# Generated by Django 2.0.2 on 2018-12-06 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20181124_0539'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=88.0, max_digits=5),
        ),
    ]
