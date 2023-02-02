# Generated by Django 4.1.1 on 2022-10-11 16:49

import catalogs.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of Catalog', max_length=100, unique=True)),
                ('file_name', models.FileField(help_text='Location of static catalog data file', upload_to='', validators=[catalogs.models.validate_catalog])),
                ('source', models.URLField(default='https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json', max_length=500)),
                ('version', models.CharField(choices=[('NIST_SP80053r5', 'NIST 800-53 r5'), ('NIST_SP80053r4', 'NIST 800-53 r4')], default='NIST_SP80053r5', max_length=24)),
                ('impact_level', models.CharField(choices=[('low', 'Low'), ('moderate', 'Moderate'), ('high', 'High')], default='moderate', help_text='FISMA impact level of the project', max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, null=True)),
            ],
            options={
                'unique_together': {('version', 'impact_level')},
            },
        ),
        migrations.CreateModel(
            name='Controls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_id', models.CharField(help_text='Catalog control ID, for example ac-1', max_length=12)),
                ('control_label', models.CharField(help_text='Catalog control label, for example AC-01', max_length=16)),
                ('sort_id', models.CharField(help_text='Catalog ID used for sorting, for example ac-01', max_length=16)),
                ('title', models.CharField(help_text='Catalog control title, for example Access Control Policy and Procedures.', max_length=124)),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogs.catalog')),
            ],
        ),
    ]