# Generated by Django 2.0.1 on 2018-01-30 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='types_id',
            field=models.IntegerField(null=True, verbose_name='类型所属表主键'),
        ),
    ]
