# Generated by Django 4.1.5 on 2023-02-21 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0009_teacher_isapproved'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='salary',
            field=models.IntegerField(default=False, max_length=100),
        ),
    ]
