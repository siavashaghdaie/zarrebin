# Generated by Django 4.0.1 on 2022-01-21 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0003_remove_podcast_subject_podcast_producer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=25, verbose_name='ارسال کننده')),
                ('subject', models.CharField(max_length=50, verbose_name='موضوع')),
                ('message', models.TextField(verbose_name='پیام')),
            ],
        ),
        migrations.AlterField(
            model_name='podcast',
            name='producer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='podcast.podcaster', verbose_name='تهیه کننده'),
        ),
    ]
