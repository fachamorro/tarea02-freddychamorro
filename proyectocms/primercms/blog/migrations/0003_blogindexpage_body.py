# Generated by Django 4.1.2 on 2022-11-01 03:36

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='body',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
