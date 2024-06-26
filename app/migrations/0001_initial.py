# Generated by Django 5.0.2 on 2024-05-13 02:22

import django.contrib.auth.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about-pic-upload/')),
                ('image_title', models.CharField(blank=True, max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AboutUsDesc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.ImageField(upload_to='about-us-bg/')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('imageDesc', models.ImageField(upload_to='about-us-image/')),
                ('mission', models.CharField(blank=True, max_length=255)),
                ('vision', models.CharField(blank=True, max_length=255)),
                ('goal', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_text', models.CharField(blank=True, max_length=100)),
                ('primary_text', models.CharField(blank=True, max_length=100)),
                ('primary_sub', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DocumentationAssistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='documentation_assistant/')),
            ],
        ),
        migrations.CreateModel(
            name='HighlightsEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, max_length=255)),
                ('image', models.ImageField(upload_to='highlights-event/')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('time', models.TimeField(blank=True, null=True)),
                ('date_to', models.DateField(blank=True, null=True, verbose_name='Start ng date')),
                ('date_from', models.DateField(blank=True, null=True, verbose_name='End ng date')),
                ('location', models.CharField(blank=True, max_length=255)),
                ('desc', models.TextField(blank=True, null=True)),
                ('link_desc', models.CharField(blank=True, max_length=255)),
                ('details', models.CharField(blank=True, max_length=100, verbose_name='Hosted By')),
                ('learn_more', models.URLField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OfficerYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(blank=True, choices=[('2020-2021', '2020-2021'), ('2021-2022', '2021-2022'), ('2022-2023', '2022-2023'), ('2023-2024', '2023-2024'), ('2024-2025', '2024-2025'), ('2025-2026', '2025-2026'), ('2026-2027', '2026-2027'), ('2027-2028', '2027-2028'), ('2028-2029', '2028-2029'), ('2029-2030', '2029-2030'), ('2030-2031', '2030-2031'), ('2031-2032', '2031-2032'), ('2032-2033', '2032-2033'), ('2033-2034', '2033-2034'), ('2034-2035', '2034-2035'), ('2035-2036', '2035-2036'), ('2036-2037', '2036-2037'), ('2037-2038', '2037-2038'), ('2038-2039', '2038-2039'), ('2039-2040', '2039-2040'), ('2040-2041', '2040-2041'), ('2041-2042', '2041-2042'), ('2042-2043', '2042-2043'), ('2043-2044', '2043-2044'), ('2044-2045', '2044-2045'), ('2045-2046', '2045-2046'), ('2046-2047', '2046-2047'), ('2047-2048', '2047-2048'), ('2048-2049', '2048-2049'), ('2049-2050', '2049-2050')], max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acct_name', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to='payment-qr/')),
            ],
        ),
        migrations.CreateModel(
            name='SoftwareTools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, max_length=255)),
                ('image', models.ImageField(upload_to='software-tools/')),
            ],
        ),
        migrations.CreateModel(
            name='SoftwareToolsResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to='software-resources/')),
                ('desc', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('username', models.CharField(max_length=100, null=True, unique=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('orgbox', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile-images/')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('sem_1', models.DateTimeField(blank=True, null=True)),
                ('sem_2', models.DateTimeField(blank=True, null=True)),
                ('year_section', models.CharField(blank=True, choices=[('1st Year', '1st Year'), ('2nd Year', '2nd Year'), ('3rd Year', '3rd Year'), ('4th Year', '4th Year')], max_length=10, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DocumentationTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=100)),
                ('documentation_head', models.CharField(max_length=100)),
                ('documentation_head_img', models.ImageField(blank=True, null=True, upload_to='documentation_head/')),
                ('assistants', models.ManyToManyField(to='app.documentationassistant')),
            ],
        ),
        migrations.CreateModel(
            name='MultimediaTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multimedia_head', models.CharField(blank=True, max_length=100)),
                ('multimedia_head_img', models.ImageField(blank=True, upload_to='multimedia_head')),
                ('multimedia_assistant_1', models.CharField(blank=True, max_length=100)),
                ('multimedia_assistant_2', models.CharField(blank=True, max_length=100)),
                ('multimedia_assistant_3', models.CharField(blank=True, max_length=100)),
                ('multimedia_assistant_4', models.CharField(blank=True, max_length=100)),
                ('multimedia_assistant_5', models.CharField(blank=True, max_length=100)),
                ('multimedia_assistant_6', models.CharField(blank=True, max_length=100)),
                ('multimedia_assistant_7', models.CharField(blank=True, max_length=100)),
                ('multimedia_assistant_8', models.CharField(blank=True, max_length=100)),
                ('multimedia_assistant_9', models.CharField(blank=True, max_length=100)),
                ('multimedia_assistant_10', models.CharField(blank=True, max_length=100)),
                ('multimedia_assistant_1_img', models.ImageField(blank=True, upload_to='multimedia_assistant')),
                ('multimedia_assistant_2_img', models.ImageField(blank=True, upload_to='multimedia_assistant')),
                ('multimedia_assistant_3_img', models.ImageField(blank=True, upload_to='multimedia_assistant')),
                ('multimedia_assistant_4_img', models.ImageField(blank=True, upload_to='multimedia_assistant')),
                ('multimedia_assistant_5_img', models.ImageField(blank=True, upload_to='multimedia_assistant')),
                ('multimedia_assistant_6_img', models.ImageField(blank=True, upload_to='multimedia_assistant')),
                ('multimedia_assistant_7_img', models.ImageField(blank=True, upload_to='multimedia_assistant')),
                ('multimedia_assistant_8_img', models.ImageField(blank=True, upload_to='multimedia_assistant')),
                ('multimedia_assistant_9_img', models.ImageField(blank=True, upload_to='multimedia_assistant')),
                ('multimedia_assistant_10_img', models.ImageField(blank=True, upload_to='multimedia_assistant')),
                ('role_assistant_1', models.CharField(blank=True, max_length=100)),
                ('role_assistant_2', models.CharField(blank=True, max_length=100)),
                ('role_assistant_3', models.CharField(blank=True, max_length=100)),
                ('role_assistant_4', models.CharField(blank=True, max_length=100)),
                ('role_assistant_5', models.CharField(blank=True, max_length=100)),
                ('role_assistant_6', models.CharField(blank=True, max_length=100)),
                ('role_assistant_7', models.CharField(blank=True, max_length=100)),
                ('role_assistant_8', models.CharField(blank=True, max_length=100)),
                ('role_assistant_9', models.CharField(blank=True, max_length=100)),
                ('role_assistant_10', models.CharField(blank=True, max_length=100)),
                ('year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.officeryear')),
            ],
        ),
        migrations.CreateModel(
            name='ExecutiveOfficer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('president', models.CharField(blank=True, max_length=100)),
                ('president_img', models.ImageField(blank=True, upload_to='president')),
                ('vp_internal', models.CharField(blank=True, max_length=100)),
                ('vp_internal_img', models.ImageField(blank=True, upload_to='vp_internal')),
                ('vp_external', models.CharField(blank=True, max_length=100)),
                ('vp_external_img', models.ImageField(blank=True, upload_to='vp_external')),
                ('secretary', models.CharField(blank=True, max_length=100)),
                ('secretary_img', models.ImageField(blank=True, upload_to='secretary')),
                ('assistant_secretary', models.CharField(blank=True, max_length=100)),
                ('assistant_secretary_img', models.ImageField(blank=True, upload_to='assistant_secretary')),
                ('treasurer', models.CharField(blank=True, max_length=100)),
                ('treasurer_img', models.ImageField(blank=True, upload_to='treasurer')),
                ('assistant_treasurer', models.CharField(blank=True, max_length=100)),
                ('assistant_treasurer_img', models.ImageField(blank=True, upload_to='assistant_treasurer')),
                ('auditor', models.CharField(blank=True, max_length=100)),
                ('auditor_img', models.ImageField(blank=True, upload_to='auditor')),
                ('pro', models.CharField(blank=True, max_length=100)),
                ('pro_img', models.ImageField(blank=True, upload_to='pro')),
                ('year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.officeryear')),
            ],
        ),
        migrations.CreateModel(
            name='EsportsTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esport_head', models.CharField(blank=True, max_length=100)),
                ('esport_head_img', models.ImageField(blank=True, upload_to='esport_head')),
                ('esport_assistant_1', models.CharField(blank=True, max_length=100)),
                ('esport_assistant_2', models.CharField(blank=True, max_length=100)),
                ('esport_assistant_3', models.CharField(blank=True, max_length=100)),
                ('esport_assistant_4', models.CharField(blank=True, max_length=100)),
                ('esport_assistant_5', models.CharField(blank=True, max_length=100)),
                ('esport_assistant_6', models.CharField(blank=True, max_length=100)),
                ('esport_assistant_7', models.CharField(blank=True, max_length=100)),
                ('esport_assistant_8', models.CharField(blank=True, max_length=100)),
                ('esport_assistant_9', models.CharField(blank=True, max_length=100)),
                ('esport_assistant_10', models.CharField(blank=True, max_length=100)),
                ('esport_assistant_1_img', models.ImageField(blank=True, upload_to='esport_assistant')),
                ('esport_assistant_2_img', models.ImageField(blank=True, upload_to='esport_assistant')),
                ('esport_assistant_3_img', models.ImageField(blank=True, upload_to='esport_assistant')),
                ('esport_assistant_4_img', models.ImageField(blank=True, upload_to='esport_assistant')),
                ('esport_assistant_5_img', models.ImageField(blank=True, upload_to='esport_assistant')),
                ('esport_assistant_6_img', models.ImageField(blank=True, upload_to='esport_assistant')),
                ('esport_assistant_7_img', models.ImageField(blank=True, upload_to='esport_assistant')),
                ('esport_assistant_8_img', models.ImageField(blank=True, upload_to='esport_assistant')),
                ('esport_assistant_9_img', models.ImageField(blank=True, upload_to='esport_assistant')),
                ('esport_assistant_10_img', models.ImageField(blank=True, upload_to='esport_assistant')),
                ('role_assistant_1', models.CharField(blank=True, max_length=100)),
                ('role_assistant_2', models.CharField(blank=True, max_length=100)),
                ('role_assistant_3', models.CharField(blank=True, max_length=100)),
                ('role_assistant_4', models.CharField(blank=True, max_length=100)),
                ('role_assistant_5', models.CharField(blank=True, max_length=100)),
                ('role_assistant_6', models.CharField(blank=True, max_length=100)),
                ('role_assistant_7', models.CharField(blank=True, max_length=100)),
                ('role_assistant_8', models.CharField(blank=True, max_length=100)),
                ('role_assistant_9', models.CharField(blank=True, max_length=100)),
                ('role_assistant_10', models.CharField(blank=True, max_length=100)),
                ('year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.officeryear')),
            ],
        ),
        migrations.CreateModel(
            name='ProgrammingTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programming_head', models.CharField(blank=True, max_length=100)),
                ('programming_head_img', models.ImageField(blank=True, upload_to='programming_head')),
                ('programming_assistant_1', models.CharField(blank=True, max_length=100)),
                ('programming_assistant_2', models.CharField(blank=True, max_length=100)),
                ('programming_assistant_3', models.CharField(blank=True, max_length=100)),
                ('programming_assistant_4', models.CharField(blank=True, max_length=100)),
                ('programming_assistant_5', models.CharField(blank=True, max_length=100)),
                ('programming_assistant_6', models.CharField(blank=True, max_length=100)),
                ('programming_assistant_7', models.CharField(blank=True, max_length=100)),
                ('programming_assistant_8', models.CharField(blank=True, max_length=100)),
                ('programming_assistant_9', models.CharField(blank=True, max_length=100)),
                ('programming_assistant_10', models.CharField(blank=True, max_length=100)),
                ('programming_assistant_1_img', models.ImageField(blank=True, upload_to='programming_assistant')),
                ('programming_assistant_2_img', models.ImageField(blank=True, upload_to='programming_assistant')),
                ('programming_assistant_3_img', models.ImageField(blank=True, upload_to='programming_assistant')),
                ('programming_assistant_4_img', models.ImageField(blank=True, upload_to='programming_assistant')),
                ('programming_assistant_5_img', models.ImageField(blank=True, upload_to='programming_assistant')),
                ('programming_assistant_6_img', models.ImageField(blank=True, upload_to='programming_assistant')),
                ('programming_assistant_7_img', models.ImageField(blank=True, upload_to='programming_assistant')),
                ('programming_assistant_8_img', models.ImageField(blank=True, upload_to='programming_assistant')),
                ('programming_assistant_9_img', models.ImageField(blank=True, upload_to='programming_assistant')),
                ('programming_assistant_10_img', models.ImageField(blank=True, upload_to='programming_assistant')),
                ('role_assistant_1', models.CharField(blank=True, max_length=100)),
                ('role_assistant_2', models.CharField(blank=True, max_length=100)),
                ('role_assistant_3', models.CharField(blank=True, max_length=100)),
                ('role_assistant_4', models.CharField(blank=True, max_length=100)),
                ('role_assistant_5', models.CharField(blank=True, max_length=100)),
                ('role_assistant_6', models.CharField(blank=True, max_length=100)),
                ('role_assistant_7', models.CharField(blank=True, max_length=100)),
                ('role_assistant_8', models.CharField(blank=True, max_length=100)),
                ('role_assistant_9', models.CharField(blank=True, max_length=100)),
                ('role_assistant_10', models.CharField(blank=True, max_length=100)),
                ('year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.officeryear')),
            ],
        ),
        migrations.CreateModel(
            name='WritersTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writers_head', models.CharField(blank=True, max_length=100)),
                ('writers_head_img', models.ImageField(blank=True, upload_to='writers_head')),
                ('writers_assistant_1', models.CharField(blank=True, max_length=100)),
                ('writers_assistant_2', models.CharField(blank=True, max_length=100)),
                ('writers_assistant_3', models.CharField(blank=True, max_length=100)),
                ('writers_assistant_4', models.CharField(blank=True, max_length=100)),
                ('writers_assistant_5', models.CharField(blank=True, max_length=100)),
                ('writers_assistant_6', models.CharField(blank=True, max_length=100)),
                ('writers_assistant_7', models.CharField(blank=True, max_length=100)),
                ('writers_assistant_8', models.CharField(blank=True, max_length=100)),
                ('writers_assistant_9', models.CharField(blank=True, max_length=100)),
                ('writers_assistant_10', models.CharField(blank=True, max_length=100)),
                ('writers_assistant_1_img', models.ImageField(blank=True, upload_to='writers_assistant')),
                ('writers_assistant_2_img', models.ImageField(blank=True, upload_to='writers_assistant')),
                ('writers_assistant_3_img', models.ImageField(blank=True, upload_to='writers_assistant')),
                ('writers_assistant_4_img', models.ImageField(blank=True, upload_to='writers_assistant')),
                ('writers_assistant_5_img', models.ImageField(blank=True, upload_to='writers_assistant')),
                ('writers_assistant_6_img', models.ImageField(blank=True, upload_to='writers_assistant')),
                ('writers_assistant_7_img', models.ImageField(blank=True, upload_to='writers_assistant')),
                ('writers_assistant_8_img', models.ImageField(blank=True, upload_to='writers_assistant')),
                ('writers_assistant_9_img', models.ImageField(blank=True, upload_to='writers_assistant')),
                ('writers_assistant_10_img', models.ImageField(blank=True, upload_to='writers_assistant')),
                ('role_assistant_1', models.CharField(blank=True, max_length=100)),
                ('role_assistant_2', models.CharField(blank=True, max_length=100)),
                ('role_assistant_3', models.CharField(blank=True, max_length=100)),
                ('role_assistant_4', models.CharField(blank=True, max_length=100)),
                ('role_assistant_5', models.CharField(blank=True, max_length=100)),
                ('role_assistant_6', models.CharField(blank=True, max_length=100)),
                ('role_assistant_7', models.CharField(blank=True, max_length=100)),
                ('role_assistant_8', models.CharField(blank=True, max_length=100)),
                ('role_assistant_9', models.CharField(blank=True, max_length=100)),
                ('role_assistant_10', models.CharField(blank=True, max_length=100)),
                ('year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.officeryear')),
            ],
        ),
    ]
