# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models
from django.conf import settings

class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_race', models.CharField(blank=True, max_length=50, verbose_name=b'Race')),
                ('github_url', models.CharField(blank=True,max_length=300, verbose_name=b'Github URL')),
                ('cover_letter_text', models.TextField(blank=True, verbose_name=b"Cover Letter")),
                ('resume_text', models.TextField(blank=True, verbose_name=b"Resume")),
                ('linkedin_url', models.CharField(verbose_name=b"LinkedIn URL", max_length=300)),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
