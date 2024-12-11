# Generated by Django 5.1.1 on 2024-12-11 14:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CedGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='ced_profile_pics')),
                ('name', models.CharField(max_length=255)),
                ('founding', models.DateField()),
                ('leader', models.CharField(max_length=100)),
                ('leader_number', models.CharField(max_length=30)),
                ('leader_profile_pic', models.ImageField(default='static/assets/user-default.png', upload_to='leader-profile')),
                ('short_description', models.CharField(max_length=255)),
                ('long_description', models.TextField(max_length=5000)),
                ('verse', models.CharField(max_length=255)),
                ('mission', models.CharField(max_length=255)),
                ('vision', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Choir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('short_description', models.CharField(max_length=255)),
                ('long_description', models.TextField(max_length=5000)),
                ('leader', models.CharField(max_length=100)),
                ('leader_number', models.CharField(max_length=30)),
                ('profile_pic', models.ImageField(upload_to='choir-profile-pics')),
            ],
        ),
        migrations.CreateModel(
            name='ChurchImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='church-images')),
            ],
        ),
        migrations.CreateModel(
            name='ChurchLeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
                ('profile_pic', models.ImageField(upload_to='leader-profile-pics')),
                ('department', models.CharField(max_length=255)),
                ('specification', models.CharField(default='Head of Department', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sermon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='sermon')),
                ('book', models.CharField(max_length=255)),
                ('verse', models.CharField(max_length=500)),
                ('description', models.TextField(max_length=5000)),
                ('preacher', models.CharField(default='Justus Mutuku', max_length=255)),
                ('preacher_number', models.CharField(default='0717740400', max_length=30)),
                ('preacher_profile_pic', models.ImageField(default='static/assets/user.png', upload_to='preacher-profile-pics')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videos')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=255)),
                ('second_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone_number', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateField(auto_now=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='personal_profile_images')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CedPracticeDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(blank=True, choices=[(1, 'Sunday'), (2, 'Monday'), (3, 'Tuesday'), (4, 'Wen'), (5, 'Thursday'), (6, 'Friday'), (7, 'Saturday')], null=True)),
                ('start', models.TimeField()),
                ('stop', models.TimeField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.cedgroup')),
            ],
        ),
        migrations.CreateModel(
            name='ChoirImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='choir-images')),
                ('choir_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.choir')),
            ],
        ),
        migrations.CreateModel(
            name='ChoirPracticeDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(blank=True, choices=[(1, 'Sunday'), (2, 'Monday'), (3, 'Tuesday'), (4, 'Wen'), (5, 'Thursday'), (6, 'Friday'), (7, 'Saturday')], null=True)),
                ('start', models.TimeField()),
                ('stop', models.TimeField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.choir')),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.CharField(max_length=255)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.sermon')),
            ],
        ),
    ]
