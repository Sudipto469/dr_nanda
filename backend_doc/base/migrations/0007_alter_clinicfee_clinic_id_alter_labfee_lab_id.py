# Generated by Django 4.1.1 on 2022-12-21 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0006_labfee"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clinicfee",
            name="clinic_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="clinicfees",
                to="base.clinic",
            ),
        ),
        migrations.AlterField(
            model_name="labfee",
            name="lab_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="labfees",
                to="base.lab",
            ),
        ),
    ]
