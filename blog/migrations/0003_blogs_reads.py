# Generated by Django 2.2.5 on 2020-06-25 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogs_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='reads',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]