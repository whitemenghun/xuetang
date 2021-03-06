# Generated by Django 2.0.1 on 2018-01-20 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0015_auto_20180120_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='ip',
            field=models.CharField(max_length=48, null=True, verbose_name='游客ip'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='user',
            field=models.ForeignKey(default='AdminAudit', on_delete=django.db.models.deletion.CASCADE, to='user.User', to_field='user', verbose_name='用户'),
        ),
    ]
