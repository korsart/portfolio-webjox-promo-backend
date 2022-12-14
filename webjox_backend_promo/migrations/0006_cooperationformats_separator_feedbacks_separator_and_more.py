# Generated by Django 4.1 on 2022-08-23 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webjox_backend_promo', '0005_servisesleadform_leadform'),
    ]

    operations = [
        migrations.AddField(
            model_name='cooperationformats',
            name='separator',
            field=models.BooleanField(default=False, verbose_name='Разделитель'),
        ),
        migrations.AddField(
            model_name='feedbacks',
            name='separator',
            field=models.BooleanField(default=False, verbose_name='Разделитель'),
        ),
        migrations.AddField(
            model_name='interview',
            name='separator',
            field=models.BooleanField(default=False, verbose_name='Разделитель'),
        ),
        migrations.AddField(
            model_name='keyses',
            name='separator',
            field=models.BooleanField(default=False, verbose_name='Разделитель'),
        ),
        migrations.AddField(
            model_name='mainblock',
            name='separator',
            field=models.BooleanField(default=False, verbose_name='Разделитель'),
        ),
        migrations.AddField(
            model_name='ourservices',
            name='separator',
            field=models.BooleanField(default=False, verbose_name='Разделитель'),
        ),
    ]
