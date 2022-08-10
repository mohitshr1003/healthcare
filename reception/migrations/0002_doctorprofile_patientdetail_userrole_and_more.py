# Generated by Django 4.0.6 on 2022-08-10 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reception', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=30)),
                ('doctor_image', models.ImageField(upload_to='doctor_img/')),
                ('doctor_dob', models.DateField()),
                ('doctor_gender', models.CharField(max_length=10)),
                ('doctor_phone', models.IntegerField()),
                ('doctor_address', models.CharField(max_length=200)),
                ('doctor_department', models.CharField(max_length=100)),
                ('doctor_qualification', models.CharField(max_length=100)),
                ('doctor_password', models.CharField(max_length=100, null=True)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PatientDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=30)),
                ('patient_gender', models.CharField(max_length=10)),
                ('patient_phone', models.IntegerField()),
                ('patient_dob', models.DateField()),
                ('patient_password', models.CharField(max_length=100)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='DoctorDetails',
        ),
        migrations.DeleteModel(
            name='PatientDetails',
        ),
    ]