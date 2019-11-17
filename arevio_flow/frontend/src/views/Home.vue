<template>
  <div class="home">
    <div class="row">
      <div class="col-6" style="display: flex; flex-direction: column-reverse">
        <b-button-toolbar class="mb-2">
          <b-button pill class="mr-2 report-action-btn" :disabled="selectedCompany === null" v-b-modal.new-report v-b-tooltip.hover title="New report"><font-awesome-icon icon="plus" /></b-button>
          <b-button pill class="mr-2 report-action-btn" :disabled="selectedRows.length == 0" v-b-modal.delete-confirm><font-awesome-icon icon="trash-alt" /></b-button>
        </b-button-toolbar>
        <b-form-select
          v-if="userdata.companies.length > 1"
          v-model="selectedCompany"
          :options="userdata.companies"
          style="width: 250px"
          class="my-3"
        ></b-form-select>
      </div>
      <div class="col-6" style="display: flex; flex-direction: column; align-items: flex-end; min-height: 75px">
        <div style="display: flex; flex-direction: row; align-items: center; height: 100%">
          <img v-if="selectedCompany" class="my-2" id="company-logo" :src="selectedCompany.logo || '/static/placeholder-company-logo.jpg'">
          <h6 v-else class="m-0">No company</h6>
        </div>
      </div>
    </div>

    <b-table ref="reportsTable"
      outlined hover
      :items="userdata.reports"
      :fields="fields"
      :filter="filter"
      :filter-included-fields="filterIncludedFields"
      selectable
      select-mode="multi"
      @row-selected="onRowSelected"
      small
    > <template v-slot:cell(actions)="row">
        <b-button variant="light" pill class="mr-2 report-action-btn text-secondary" @click="onClickDownloadReport(row.item)" v-b-tooltip.hover title="Download">
          <font-awesome-icon icon="file-download" />
        </b-button>
        <b-button variant="light" pill class="mr-2 report-action-btn text-secondary" @click="onClickUploadReport(row.item)" v-b-tooltip.hover title="Upload">
          <font-awesome-icon icon="file-upload" />
        </b-button>
        <b-button variant="light" pill class="mr-2 report-action-btn text-secondary" v-b-modal.notyetimplemented v-b-tooltip.hover title="HTML Preview">
          <font-awesome-icon icon="eye" />
        </b-button>
        <b-button variant="light" pill class="mr-2 report-action-btn text-secondary" @click="onClickRename(row.item)" v-b-tooltip.hover title="Rename">
          <font-awesome-icon icon="pen" />
        </b-button>
        <b-button variant="light" pill class="mr-2 report-action-btn text-secondary" @click="onClickDeleteReport(row.item)" v-b-tooltip.hover title="Delete">
          <font-awesome-icon icon="trash-alt" />
        </b-button>
      </template>
    </b-table>

    <b-modal id="new-report"
      centered
      title="Create a new report"
      @ok="newReport"
      @shown="initNewReportModal"
      hide-header-close
      header-bg-variant="light"
    > <h6>Name</h6>
      <b-form-input v-model="newReportName" placeholder="Enter the report name" autofocus></b-form-input><br>
      <h6>Taxonomy:</h6>
      <b-form-select
        v-model="newReportTaxonomy"
        :options="userdata.taxonomies"
        value-field="id"
        text-field="name"
        style="width: 250px"
      ></b-form-select>
    </b-modal>

    <b-modal id="delete-confirm" title="Delete report" @ok="DeleteReports" ok-title="Yes" cancel-title="No"
      hide-header-close auto-focus-button="ok"
      header-bg-variant="light"
    >
      <h6>Are you sure you want to permanently delete {{ clickedReport ? 'this report' : 'these report(s)' }}?</h6>
      {{ clickedReport ? clickedReport.name : selectedRows.map(a => a.name).join(', ') }}
    </b-modal>

    <b-modal id='spinner-modal'
      centered
      hide-footer
      hide-header
      no-close-on-backdrop
      no-close-on-esc
    > <div class="text-center">
        <b-spinner></b-spinner>
      </div>
    </b-modal>

    <b-modal id='upload-done-modal'
      :title="uploadModalTitle"
      centered
      :size="(uploadLog && uploadLog.errors.length) ? 'lg' : 'md'"
      ok-only
      scrollable
    > <div v-if="uploadLog && (uploadLog.errors.length || !uploadLog.success)">
        <div v-for="error in uploadLog.errors">
          <span class="font-weight-bold">{{ error.level }}: </span> {{ error.msg }}
        </div>
      </div>
      <p v-else>Congratulations</p>
    </b-modal>

    <b-form-file id="myFileInput"
      v-model="file"
      @input="onFileInput"
      class="d-none"
      ref="myFileInput"
    ></b-form-file>

    <b-modal id="rename"
      @ok="onRename"
      :title='`Rename "${clickedReport && clickedReport.name}"`'
      :ok-disabled="newReportName == ''"
      centered
    > <b-form-input v-model="newReportName" placeholder="Enter a new name" autofocus></b-form-input>
    </b-modal>

  </div>
</template>

<script>
import { CSRF_TOKEN } from "@/common/csrf_token.js"
import download from 'downloadjs'
export default {
  name: 'home',
  props: ['userdata'],
  computed: {
    filter: function () {
      try {
        return this.selectedCompany.id.toString();
      } catch (err) {
        return null;
      }
    },
    uploadModalTitle() {
      if (this.uploadLog == null)
        return '';
      if (this.uploadLog.success == false)
        return 'Import failed';
      if (this.uploadLog.errors.length > 0)
        return 'Import succeeded with errors';
      return 'Import succeeded without any errors';
    },
  },
  data() {
    return {
      selectedCompany: this.userdata.companies[0].value,
      fields: [
        {
          key: 'name',
          sortable: true,
          formatter: value => value ? value : "No name",
        },
        {
          key: 'taxonomy',
          sortable: true,
          formatter: value => this.userdata.taxonomyNames[value],
        },
        {
          key: 'updated_at',
          sortable: true,
          formatter: value => new Date(value).toLocaleString(),
        },
        {
          key: 'updated_by_user',
          sortable: true,
        },
        'actions',
      ],
      filterIncludedFields: ['company'],
      newReportName: null,
      newReportTaxonomy: this.userdata.taxonomies[0].id,
      selectedRows: [],
      file: null,
      clickedReport: null,
      uploadReportId: null,
      uploadLog: null,
    }
  },
  methods: {
    onRowSelected(items) {
      this.selectedRows = items;
    },
    newReport() {
      fetch('/annualreports/', {
        method: "POST",
        body: JSON.stringify({
          company: this.selectedCompany.id,
          taxonomy: this.newReportTaxonomy,
          name: this.newReportName,}),
        headers: {
          'X-CSRFTOKEN': CSRF_TOKEN,
          'Content-Type': 'application/json'},
        }).then(() => this.$emit('fetchData'))
    },
    onClickDeleteReport(item) {
      this.clickedReport = item;
      this.$bvModal.show('delete-confirm');
    },
    DeleteReports() {
      let rowsToDelete;
      if (this.clickedReport)
        rowsToDelete = [this.clickedReport];
      else
        rowsToDelete = [...this.selectedRows];
      rowsToDelete.forEach(row => {
        fetch(`/annualreports/${row.id}/`, {
          method: "DELETE",
          headers: {'X-CSRFTOKEN': CSRF_TOKEN},
        }).then(() => this.$emit('fetchData'))
      });
    },
    initNewReportModal() {
      this.newReportName = "";
    },
    onClickDownloadReport(item) {
      this.$bvModal.show('spinner-modal');
      fetch(`/annualreports/${item.id}/`, {
          method: "GET",
          headers: {'X-CSRFTOKEN': CSRF_TOKEN},
        }).then(resp => {
          return resp.blob();
        }).then(blob => {
          this.$bvModal.hide('spinner-modal');
          download(blob, `${item.name}.xlsx`);
        });
    },
    onClickUploadReport(item) {
      this.uploadLog = null;
      this.uploadReportId = item.id;
      document.getElementById('myFileInput').click();
    },
    onFileInput(file) {
      if (file === null)
        return;
      this.$refs.myFileInput.reset();
      this.$bvModal.show('spinner-modal');
      let formData = new FormData();
      formData.append('excel_file', file);
      fetch(`/annualreports/${this.uploadReportId}/`, {
        method: 'POST',
        headers: {'X-CSRFTOKEN': CSRF_TOKEN,},
        body: formData,
      }).then(resp => {
        return resp.json();
      }).then(json => {
        let parser = new DOMParser();
        let xmlDoc = parser.parseFromString(json.log,"text/xml");
        json.errors = [];
        for (let entry of xmlDoc.getElementsByTagName('entry')) {
          if (entry.attributes.level.value != "info") {
            json.errors.push({
              level: entry.attributes.level.value,
              msg: entry.textContent,
            });
          }
        }
        this.uploadLog = json;
        this.$bvModal.hide('spinner-modal');
        this.$bvModal.show('upload-done-modal');
        this.$emit('fetchData');
      });
    },
    onClickRename(item) {
      this.newReportName = '';
      this.clickedReport = item;
      this.$bvModal.show('rename');
    },
    onRename() {
      let body = new URLSearchParams();
      body.append('newName', this.newReportName);
      fetch(`/annualreports/${this.clickedReport.id}/`, {
        method: "PUT",
        body: body,
        headers: {
          'X-CSRFTOKEN': CSRF_TOKEN,
          'Content-Type': 'application/x-www-form-urlencoded'},
        }).then(() => {
          this.$emit('fetchData')
        });
    },
  },
  mounted() {
    this.$root.$on('bv::modal::hide', (bvEvent, modalId) => {
      this.clickedReport = null;
    })
  }
};
</script>

<style>
#company-logo {
    max-width: 150px;
    height: 75px;
    object-fit: contain;
}
.table td {
  vertical-align: middle;
}
.report-action-btn {
  height: 40px;
  width: 40px;
}
td > button > svg {
    margin-left: -100%;
    margin-right: -100%;
}
#spinner-modal > div {
  width: 100px;
}
</style>
