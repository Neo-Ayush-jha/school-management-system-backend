# Generated by Django 4.1.5 on 2023-02-21 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0007_student_rf_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(choices=[('English', 'English'), ('Maths', 'Maths'), ('Hindi', 'Hindi'), ('Science', 'Science'), ('S.St', 'S.St'), ('Sanskrit', 'Sanskrit'), ('Computer', 'Computer'), ('Drawing', 'Drawing'), ('P.T', 'P.T'), ('Evs', 'Evs'), ('G.k', 'G.k'), ('Urdu', 'Urdu'), ('Hindi Grammer', 'Hindi Grammer'), ('English Grammer', 'English Grammer')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=150)),
                ('t_contact', models.IntegerField()),
                ('t_email', models.EmailField(max_length=254)),
                ('t_dob', models.DateField()),
                ('t_address', models.TextField()),
                ('t_gender', models.CharField(choices=[('M', 'male'), ('F', 'female'), ('O', 'other')], max_length=10)),
                ('t_subject', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='school_management.subject', unique=True)),
            ],
        ),
    ]