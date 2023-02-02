# Generated by Django 4.1.1 on 2022-10-11 16:49

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('components', '0001_initial'),
        ('catalogs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Name of the project', max_length=100)),
                ('acronym', models.CharField(help_text='Acronym for the name of the project', max_length=20)),
                ('impact_level', models.CharField(choices=[('low', 'Low'), ('moderate', 'Moderate'), ('high', 'High')], help_text='FISMA impact level of the project', max_length=20)),
                ('catalog_version', models.CharField(default=None, help_text='The Catalog version, for example ARS 3.1', max_length=32)),
                ('location', models.CharField(choices=[('aws', 'AWS Commercial East-West'), ('govcloud', 'AWS GovCloud'), ('azure', 'Microsoft Azure'), ('other', 'Other')], default=None, help_text='Where the project is located', max_length=100, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('archived', 'Archived')], default='active', help_text='Status of the project', max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('catalog', models.ForeignKey(default=None, help_text='Catalog id that this project uses', on_delete=django.db.models.deletion.PROTECT, related_name='projects_catalog', to='catalogs.catalog')),
                ('components', models.ManyToManyField(blank=True, help_text='Components that exist in the project', related_name='used_by_projects', to='components.component')),
            ],
            options={
                'permissions': [('can_add_members', 'Can add members'), ('can_delete_members', 'Can delete members'), ('manage_project_users', 'Can manage users on project')],
            },
        ),
        migrations.CreateModel(
            name='ProjectControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('not_started', 'Not started'), ('incomplete', 'Incomplete'), ('complete', 'Complete'), ('not_applicable', 'Not applicable')], default='not_started', help_text='The Project Control status; completed, incomplete, or not started', max_length=20)),
                ('remarks', models.TextField(blank=True)),
                ('disabled_narratives', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None)),
                ('control', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='to_control', to='catalogs.controls')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_project', to='projects.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='controls',
            field=models.ManyToManyField(related_name='project_controls', through='projects.ProjectControl', to='catalogs.controls'),
        ),
        migrations.AddField(
            model_name='project',
            name='creator',
            field=models.ForeignKey(help_text='User id of the project creator', on_delete=django.db.models.deletion.PROTECT, related_name='projects_created', to=settings.AUTH_USER_MODEL),
        ),
    ]