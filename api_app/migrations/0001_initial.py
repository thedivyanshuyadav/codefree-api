# Generated by Django 2.2.24 on 2021-11-19 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IrisModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sepal_length', models.CharField(max_length=255)),
                ('sepal_width', models.CharField(max_length=255)),
                ('petal_length', models.CharField(max_length=255)),
                ('petal_width', models.CharField(max_length=255)),
                ('iris_class', models.CharField(max_length=255)),
            ],
        ),
    ]
