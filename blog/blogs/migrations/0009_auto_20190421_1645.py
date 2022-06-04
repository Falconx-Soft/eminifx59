# Generated by Django 2.0.4 on 2019-04-21 11:45

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_auto_20190421_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='video_link',
        ),
        migrations.AddField(
            model_name='blog',
            name='video',
            field=embed_video.fields.EmbedVideoField(default=0),
            preserve_default=False,
        ),
    ]