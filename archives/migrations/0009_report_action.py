# Generated by Django 3.2.9 on 2021-12-31 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0008_alter_report_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='action',
            field=models.SmallIntegerField(default=0),
        ),
    ]
