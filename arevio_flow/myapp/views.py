from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from . import serializers, models
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, Http404, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from django.conf import settings
from datetime import datetime
import os, shutil

class IndexTemplateView(LoginRequiredMixin, TemplateView):
    """
    Entry point view for the frontend.
    """
    def get_template_names(self):
        # if settings.DEBUG:
        #     template_name = 'index-dev.html'
        # else:
        #     template_name = 'index.html'
        template_name = 'index-dev.html'
        return template_name

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('entry-point')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def get_company_qs(request):
    if request.user.is_superuser:
        return models.Company.objects.all()
    return request.user.company_set.all()

def get_annualreport_qs(request):
    if request.user.is_superuser:
        return models.AnnualReport.objects.all()
    return models.AnnualReport.objects.filter(company__in=get_company_qs(request))

@login_required
def userdata(request):
    data = serializers.UserSerializer(request.user).data
    taxonomies = models.Taxonomy.objects.all()
    companies = get_company_qs(request)
    reports = get_annualreport_qs(request)
    data['companies'] = serializers.CompanySerializer(companies, many=True).data
    data['taxonomies'] = serializers.TaxonomySerializer(taxonomies, many=True).data
    data['reports'] = serializers.AnnualReportSerializer(reports, many=True).data
    return JsonResponse(data)

def update_and_save_report(report, request):
    report.updated_by_user = request.user
    report.updated_at = datetime.now()
    report.save()
    return report

def rm(file):
    try: os.remove(file)
    except: pass

def get_arelle_command(report, xbrl_file):
    return " ".join([
        os.path.join(settings.ARELLE_HOME, 'arelleCmdLine'),
        report.taxonomy.arelleCmdLine_options.replace(
            "%ARELLE_HOME%", settings.ARELLE_HOME),
        '-f', xbrl_file])

class AnnualReportList(APIView):
    def post(self, request):
        serializer = serializers.AnnualReportSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if not serializer.validated_data['company'] in get_company_qs(request):
            raise PermissionDenied
        new_report = serializer.save()
        new_report = update_and_save_report(new_report, request)
        shutil.copy(
            new_report.taxonomy.xbrl_template.path,
            os.path.join(settings.XBRL_DIR, f'{new_report.id}.xbrl'),
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AnnualReportDetail(APIView):
    def get_object(self, request, pk):
        try:
            return get_annualreport_qs(request).get(pk=pk)
        except:
            raise Http404

    def delete(self, request, pk):
        report = self.get_object(request, pk)
        xbrl_file = os.path.join(settings.XBRL_DIR, f'{report.id}.xbrl')
        excel_file = os.path.join(settings.XBRL_DIR, f'{report.id}.xlsx')
        rm(xbrl_file)
        rm(excel_file)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, pk):
        report = self.get_object(request, pk)
        xbrl_file = os.path.join(settings.XBRL_DIR, f'{report.id}.xbrl')
        excel_file = os.path.join(settings.XBRL_DIR, f'{report.id}.xlsx')
        file_type = request.GET.get('file_type', 'xlsx')
        if file_type == 'xlsx':
            cmd = get_arelle_command(report, xbrl_file)
            cmd += ' --save-XLSX-rw=' + excel_file
            os.system(cmd)
        with open(excel_file if file_type == 'xlsx' else xbrl_file, 'rb') as f:
            response = HttpResponse(f.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = f'inline; filename={report.name}.xlsx'
            return response
        raise Http404

    def post(self, request, pk):
        report = self.get_object(request, pk)
        xbrl_file = os.path.join(settings.XBRL_DIR, f'{report.id}.xbrl')
        excel_file = os.path.join(settings.XBRL_DIR, f'{report.id}.xlsx')
        if request.FILES['excel_file'].size > 25000000:
            return HttpResponseBadRequest('File size bigger than 25MB!')
        time1 = os.path.getmtime(xbrl_file)
        with open(excel_file, 'wb') as f:
            f.write(request.FILES['excel_file'].read())
        rm(settings.ARELLE_LOGFILE)
        cmd = get_arelle_command(report, xbrl_file)
        cmd += ' --load-XLSX=' + excel_file
        cmd += ' --logFile=' + settings.ARELLE_LOGFILE
        os.system(cmd)
        time2 = os.path.getmtime(xbrl_file)
        success = time1 != time2    # Arevio modified the file means success
        if success:
            update_and_save_report(report, request)
        response = {}
        response['success'] = success
        with open(settings.ARELLE_LOGFILE, 'r') as f:
            response['log'] = f.read()
        return JsonResponse(response)

    def put(self, request, pk):
        try:
            newName = request.POST.get('newName')
        except:
            raise PermissionDenied
        report = self.get_object(request, pk)
        report.name = newName
        update_and_save_report(report, request)
        return HttpResponse('OK')
