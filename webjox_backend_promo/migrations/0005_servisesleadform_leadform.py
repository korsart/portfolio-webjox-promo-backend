# Generated by Django 4.1 on 2022-08-23 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webjox_backend_promo', '0004_feedback_feedbacks'),
    ]

    operations = [
        migrations.AddField(
            model_name='servisesleadform',
            name='leadform',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='webjox_backend_promo.leadform'),
        ),
    ]
