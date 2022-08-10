# Generated by Django 4.0.6 on 2022-08-05 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0003_patientdetails_delete_patientdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctordetail',
            name='doctor_id',
            field=models.CharField(max_length=6, unique=True),
        ),
        migrations.AlterField(
            model_name='doctordetail',
            name='doctor_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='doctordetail',
            name='doctor_phone',
            field=models.IntegerField(),
        ),
    ]
