# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=25)),
                ('calories', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FruitEaten',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('qty', models.IntegerField(verbose_name='quantity', default=0)),
                ('fruit', models.ForeignKey(to='blog.Fruit')),
                ('post', models.ForeignKey(to='blog.Post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='ate',
            field=models.ManyToManyField(to='blog.Fruit', through='blog.FruitEaten'),
        ),
        migrations.AlterUniqueTogether(
            name='fruiteaten',
            unique_together=set([('post', 'fruit')]),
        ),
    ]
