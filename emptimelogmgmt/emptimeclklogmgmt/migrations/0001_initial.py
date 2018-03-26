# Generated by Django 2.0.3 on 2018-03-25 22:09

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('recovery_answer', models.CharField(max_length=20)),
                ('recovery_email', models.CharField(max_length=50)),
                ('last_updated_on', models.DateTimeField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=40)),
                ('middle_name', models.CharField(blank=True, default='', max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_on', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('recovery_answer', models.CharField(max_length=20)),
                ('recovery_email', models.CharField(max_length=20)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated_on', models.DateTimeField(blank=True, null=True)),
                ('deleted_on', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('middle_name', models.CharField(blank=True, default='', max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('department', models.CharField(default='', max_length=50)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_on', models.DateTimeField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emptimeclklogmgmt.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_status', models.CharField(max_length=30)),
                ('notes', models.CharField(blank=True, default='', max_length=100)),
                ('time', models.TimeField(default=django.utils.timezone.localtime)),
                ('date', models.DateField(default=datetime.date.today)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emptimeclklogmgmt.Employee')),
            ],
        ),
    ]
