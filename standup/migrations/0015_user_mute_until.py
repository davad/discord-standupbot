# Generated by Django 2.2.6 on 2019-11-17 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standup', '0014_standuptype_public_publish_after'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mute_until',
            field=models.DateField(blank=True, null=True),
        ),
    ]
