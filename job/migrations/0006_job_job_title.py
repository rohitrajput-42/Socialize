# Generated by Django 3.1.2 on 2021-08-04 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_job_applicants'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_title',
            field=models.CharField(default=0, max_length=600),
            preserve_default=False,
        ),
    ]
