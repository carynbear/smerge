# Generated by Django 2.0.2 on 2018-02-02 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('picture', models.FileField(blank=True,
                                             null=True, upload_to='', verbose_name='Picture')),
                ('description', models.CharField(blank=True,
                                                 max_length=200, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='SnapFile',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(
                    auto_now_add=True, verbose_name='Timestamp')),
                ('file', models.FileField(upload_to='', verbose_name='File')),
                ('user', models.CharField(
                    max_length=30, null=True, verbose_name='user')),
                ('ancestors', models.ManyToManyField(to='home.SnapFile')),
                ('project', models.ForeignKey(
                    on_delete=models.CASCADE, to='home.Project')),
            ],
            options={
                'verbose_name': 'SnapFile',
                'verbose_name_plural': 'SnapFiles',
            },
        ),
    ]
