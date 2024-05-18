# Generated by Django 4.0.1 on 2022-01-21 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Podcaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personId', models.IntegerField(verbose_name='شماره')),
                ('firstName', models.CharField(max_length=25, verbose_name='نام')),
                ('lastName', models.CharField(max_length=25, verbose_name='نام خانوادگی')),
                ('position', models.CharField(max_length=25, verbose_name='مسئولیت')),
                ('about', models.TextField(verbose_name='درباره ی من')),
                ('pic', models.ImageField(upload_to='', verbose_name='تصویر')),
            ],
        ),
        migrations.CreateModel(
            name='Podcasts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('podcastID', models.IntegerField(verbose_name='شماره آرشیو')),
                ('description', models.TextField(verbose_name='درباره\u200cی اپیزود')),
                ('highlights', models.TextField(verbose_name='جان مایه')),
                ('name', models.CharField(max_length=25, verbose_name='نام')),
                ('episodeNum', models.IntegerField(verbose_name='شماره ی اپیزود')),
                ('subject', models.CharField(max_length=25, verbose_name='موضوع')),
                ('cast', models.TextField(verbose_name='عوامل')),
                ('publishDate', models.DateField(verbose_name='تاریخ')),
                ('music', models.TextField(verbose_name='موسیقی ها')),
                ('pic', models.ImageField(upload_to='', verbose_name='تصویر')),
            ],
        ),
    ]