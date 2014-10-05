# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=36)),
                ('price', models.PositiveIntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='order date')),
                ('status', models.PositiveSmallIntegerField(default=1, choices=[(1, 'ordered'), (2, 'in progress'), (3, 'on the road'), (4, 'delivered')])),
                ('created_by', models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL)),
                ('ingredients', models.ManyToManyField(to='shop.Ingredient')),
            ],
            options={
                'ordering': ('-created_at',),
            },
            bases=(models.Model,),
        ),
    ]
