# Generated by Django 3.1.7 on 2021-04-10 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210409_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_colours',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
