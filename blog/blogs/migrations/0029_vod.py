# Generated by Django 3.2.13 on 2022-06-03 19:10

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0028_contact_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='vod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
        ),
    ]
