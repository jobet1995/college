# Generated by Django 3.2.25 on 2024-05-18 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emergency_contact', '0001_initial'),
        ('enrollment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='emergency',
            field=models.ForeignKey(default=0.00018379281537176273, on_delete=django.db.models.deletion.CASCADE, to='emergency_contact.emergency'),
            preserve_default=False,
        ),
    ]