# Generated by Django 4.2.11 on 2024-05-11 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gauth', '0002_remove_gauthuser_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='gauthuser',
            name='user_id',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
