# Generated by Django 4.1.5 on 2023-02-21 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0010_teacher_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='salary',
            field=models.IntegerField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
