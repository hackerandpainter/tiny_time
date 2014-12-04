# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'\xe6\x97\xa0\xe5\x90\x8d', max_length=50)),
                ('artistId', models.IntegerField()),
                ('artist', models.CharField(default=b'\xe6\x97\xa0\xe5\x90\x8d', max_length=50)),
                ('categoryId', models.IntegerField()),
                ('category', models.CharField(default=b'\xe6\x99\xae\xe9\x80\x9a', max_length=50)),
                ('vol', models.CharField(default=b'2014000000', max_length=50)),
                ('like', models.IntegerField()),
                ('share', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('paintings', models.CharField(default=b'', max_length=1000)),
            ],
            options={
                'ordering': ('id',),
            },
            bases=(models.Model,),
        ),
    ]
