# Generated by Django 4.0.1 on 2022-02-11 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0007_remove_podcast_podcastid'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='castboxlink',
            field=models.TextField(null=True, verbose_name='لینک کست باکس'),
        ),
    ]
