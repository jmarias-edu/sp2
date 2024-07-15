# Generated by Django 4.2.11 on 2024-07-15 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_variantread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variantread',
            name='genomeURL',
            field=models.URLField(blank=True, default=None, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='variantread',
            name='variantURL',
            field=models.URLField(blank=True, default=None, max_length=256, null=True),
        ),
        migrations.CreateModel(
            name='UploadedProjectFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=projects.models.fileDirectory)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.variantread')),
            ],
        ),
    ]
