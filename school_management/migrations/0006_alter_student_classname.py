# Generated by Django 4.1.5 on 2023-02-17 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0005_student_isapproved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='className',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_management.classes'),
        ),
    ]
