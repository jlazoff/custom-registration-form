# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms import widgets
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
                ('github_url', models.CharField(blank=True,max_length=300, verbose_name=b'Github')),
                ('linkedin_url', models.CharField(verbose_name=b"LinkedIn/Portfolio/Personal Website", max_length=300, null=True)),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]