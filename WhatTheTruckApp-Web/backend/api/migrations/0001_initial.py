# Generated by Django 5.1.6 on 2025-02-25 19:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='WTT_Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logID', models.IntegerField()),
                ('userID', models.IntegerField()),
                ('truckID', models.IntegerField()),
                ('trailerID', models.IntegerField()),
                ('trip', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('load', models.IntegerField()),
                ('height', models.IntegerField()),
                ('defects_en_route', models.CharField(max_length=1000)),
                ('incidents', models.CharField(max_length=1000)),
                ('remarks', models.CharField(max_length=1000)),
                ('pictures', models.CharField(max_length=100)),
                ('declaration', models.IntegerField()),
                ('signature', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'WTT_Log',
            },
        ),
        migrations.CreateModel(
            name='WTT_Log_Inspect_Items',
            fields=[
                ('itemID', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'WTT_Log_Inspect_Items',
            },
        ),
        migrations.CreateModel(
            name='WTT_Trailer',
            fields=[
                ('trailerID', models.AutoField(primary_key=True, serialize=False)),
                ('make_model', models.CharField(max_length=30)),
                ('license_plate', models.CharField(max_length=8)),
                ('carrier', models.CharField(max_length=30)),
                ('jurisdiction', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'WTT_Trailer',
            },
        ),
        migrations.CreateModel(
            name='WTT_Truck',
            fields=[
                ('truckID', models.AutoField(primary_key=True, serialize=False)),
                ('make_model', models.CharField(max_length=30)),
                ('license_plate', models.CharField(max_length=8)),
                ('odometer', models.IntegerField()),
                ('carrier', models.CharField(max_length=30)),
                ('jurisdiction', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'WTT_Truck',
            },
        ),
        migrations.CreateModel(
            name='WTT_User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('employeeID', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=1)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('driver_license', models.CharField(max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'WTT_User',
            },
        ),
        migrations.CreateModel(
            name='WTT_Log_Inspect_Det',
            fields=[
                ('logID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.wtt_log')),
                ('itemID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.wtt_log_inspect_items')),
            ],
            options={
                'db_table': 'WTT_Log_Inspect_Det',
            },
        ),
    ]
