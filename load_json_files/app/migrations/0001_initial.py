# Generated by Django 3.2.4 on 2021-06-11 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files_temp/', verbose_name='Upload Files')),
                ('uploaded_on', models.DateTimeField(auto_now_add=True, verbose_name='Uploaded On')),
            ],
            options={
                'db_table': 'file_session',
            },
        ),
        migrations.CreateModel(
            name='file_Json_data',
            fields=[
                ('user_id', models.IntegerField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=144)),
                ('body', models.TextField()),
                ('files_id', models.IntegerField()),
            ],
            options={
                'db_table': 'file_j_data',
            },
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/', verbose_name='Upload Files')),
                ('uploaded_on', models.DateTimeField(auto_now_add=True, verbose_name='Uploaded On')),
            ],
            options={
                'db_table': 'files',
            },
        ),
        migrations.CreateModel(
            name='files_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json_data', models.IntegerField()),
                ('files', models.IntegerField()),
            ],
            options={
                'db_table': 'files_data',
            },
        ),
    ]
