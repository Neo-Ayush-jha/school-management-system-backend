# Generated by Django 4.1.5 on 2023-02-15 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0004_alter_student_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='isApproved',
            field=models.BooleanField(default=False),
        ),
    ]
