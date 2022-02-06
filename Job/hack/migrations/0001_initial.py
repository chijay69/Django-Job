# Generated by Django 4.0 on 2022-02-05 09:47

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('by', models.CharField(max_length=150, null=True)),
                ('descendants', models.IntegerField(blank=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('time', models.IntegerField(null=True)),
                ('title', models.TextField(max_length=200, null=True)),
                ('type', models.CharField(max_length=10)),
                ('url', models.URLField(null=True)),
                ('kids', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None)),
                ('deleted', models.BooleanField(default=False, null=True)),
                ('dead', models.BooleanField(default=False, null=True)),
                ('text', models.TextField(blank=True, max_length=500, null=True, verbose_name='text')),
                ('parent', models.IntegerField(blank=True, null=True)),
                ('parts', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None)),
            ],
            options={
                'ordering': ('-type',),
            },
        ),
    ]
