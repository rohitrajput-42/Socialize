# Generated by Django 3.1.2 on 2021-08-08 09:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0024_auto_20210808_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=350)),
                ('content', ckeditor.fields.RichTextField()),
                ('author', models.CharField(blank=True, max_length=350, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='like',
            name='value',
            field=models.CharField(choices=[('Unlike', 'Unlike'), ('Like', 'Like')], max_length=10),
        ),
    ]
