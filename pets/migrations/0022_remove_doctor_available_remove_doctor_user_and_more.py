# Generated by Django 5.0.2 on 2024-09-29 14:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0021_doctor_consultation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='available',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='user',
        ),
        migrations.AddField(
            model_name='doctor',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='doctor',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=9)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availabilities', to='pets.doctor')),
            ],
        ),
        migrations.DeleteModel(
            name='Consultation',
        ),
    ]
