# Generated by Django 3.1.7 on 2021-05-09 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=25)),
                ('student_email', models.EmailField(max_length=254, unique=True)),
                ('ssc_marks', models.IntegerField()),
                ('inter_marks', models.IntegerField()),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StaffRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_dept', models.CharField(choices=[('CE', 'Civil Engineering'), ('CSE', 'Computer Science Engineering'), ('ECE', 'Electronics Communtication Engineering'), ('EEE', 'Electronics Electrical Engineering'), ('ME', 'Mechanical Engineering')], default=None, max_length=3)),
                ('staff_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default=None, max_length=1)),
                ('staff_mob', models.IntegerField()),
                ('qualification', models.TextField(max_length=10)),
                ('experience', models.CharField(max_length=10)),
                ('staff_pic', models.ImageField(upload_to='', verbose_name='pictures/')),
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='staff_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('CE', 'Civil Engineering'), ('CSE', 'Computer Science Engineering'), ('ECE', 'Electronics Communtication Engineering'), ('EEE', 'Electronics Electrical Engineering'), ('ME', 'Mechanical Engineering')], default=None, max_length=3)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default=None, max_length=1)),
                ('mobile', models.IntegerField()),
                ('profile_pic', models.ImageField(upload_to='', verbose_name='pictures/')),
                ('father_name', models.CharField(max_length=25)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_info', to=settings.AUTH_USER_MODEL)),
                ('student_app', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='WebApp.studentapplication')),
            ],
        ),
    ]