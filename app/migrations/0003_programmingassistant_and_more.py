# Generated by Django 5.0.2 on 2024-05-13 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_documentationteam_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgrammingAssistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='programming_assistant/')),
            ],
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='programming_assistant_1',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='programming_assistant_10',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='programming_assistant_10_img',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='programming_assistant_1_img',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='programming_assistant_2',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='programming_assistant_2_img',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='programming_assistant_3',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='programming_assistant_3_img',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='programming_assistant_4',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='programming_assistant_4_img',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='programming_assistant_5',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='programming_assistant_5_img',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='programming_assistant_6',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='programming_assistant_6_img',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='programming_assistant_7',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='programming_assistant_7_img',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='programming_assistant_8',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='programming_assistant_8_img',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='programming_assistant_9',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='programming_assistant_9_img',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='role_assistant_1',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='role_assistant_10',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='role_assistant_2',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='role_assistant_3',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='role_assistant_4',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='role_assistant_5',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='role_assistant_6',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='role_assistant_7',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='role_assistant_8',
        ),
        migrations.RemoveField(
            model_name='programmingteam',
            name='role_assistant_9',
        ),
        migrations.AlterField(
            model_name='programmingteam',
            name='programming_head',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='programmingteam',
            name='programming_head_img',
            field=models.ImageField(blank=True, null=True, upload_to='programming_head/'),
        ),
        migrations.AddField(
            model_name='programmingteam',
            name='assistants',
            field=models.ManyToManyField(to='app.programmingassistant'),
        ),
    ]
