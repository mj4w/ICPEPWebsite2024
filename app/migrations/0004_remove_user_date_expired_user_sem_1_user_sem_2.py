# Generated by Django 5.0.2 on 2024-05-11 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_user_date_expired'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_expired',
        ),
        migrations.AddField(
            model_name='user',
            name='sem_1',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='sem_2',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
