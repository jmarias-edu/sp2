# Generated by Django 4.2.11 on 2024-10-03 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_variantcallproject_folder'),
    ]

    operations = [
        migrations.AddField(
            model_name='variantcallproject',
            name='status',
            field=models.CharField(blank=True, default='pending', max_length=40, null=True),
        ),
    ]
