# Generated by Django 3.1.2 on 2021-08-06 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0021_auto_20210806_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='value',
            field=models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], max_length=10),
        ),
    ]
