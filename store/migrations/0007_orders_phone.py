# Generated by Django 4.2 on 2023-05-15 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
