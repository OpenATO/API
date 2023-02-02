# Generated by Django 4.1.1 on 2022-10-11 16:49

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Name of the component', max_length=100, unique=True)),
                ('description', models.CharField(blank=True, help_text='Description of the component', max_length=500)),
                ('type', models.CharField(blank=True, help_text='Type category of the component', max_length=100, null=True)),
                ('supported_catalog_versions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('NIST_SP80053r5', 'NIST 800-53 r5'), ('NIST_SP80053r4', 'NIST 800-53 r4')], max_length=16), help_text='Catalog versions that this component is defined on.', size=None)),
                ('controls', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, help_text='List of controls that the component addresses', null=True, size=None)),
                ('search_terms', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), help_text='List of keywords to search for the component', null=True, size=None)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('component_json', models.JSONField(blank=True, help_text='OSCAL JSON representation of the component', null=True)),
                ('component_file', models.FileField(blank=True, help_text='Upload an OSCAL formatted JSON Component file', null=True, upload_to='')),
                ('status', models.IntegerField(choices=[(1, 'System Specific'), (2, 'Public')], default=2)),
            ],
        ),
    ]