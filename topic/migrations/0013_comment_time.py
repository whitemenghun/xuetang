# Generated by Django 2.0.1 on 2018-01-19 11:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0012_auto_20180119_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='评论时间'),
            preserve_default=False,
        ),
    ]