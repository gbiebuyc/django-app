# Generated by Django 2.2.4 on 2019-11-11 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_taxonomy_arellecmdline_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxonomy',
            name='xbrl_template',
            field=models.FileField(default='whatever', upload_to=''),
            preserve_default=False,
        ),
    ]
