# Generated by Django 3.2.25 on 2024-05-17 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course_name', models.CharField(max_length=255)),
                ('course_description', models.TextField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
