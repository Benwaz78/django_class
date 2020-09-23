# Generated by Django 3.0.3 on 2020-09-18 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_desc',
            field=models.TextField(blank=True, null=True, verbose_name='Category Description'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_name',
            field=models.CharField(max_length=100, verbose_name='Category'),
        ),
    ]
