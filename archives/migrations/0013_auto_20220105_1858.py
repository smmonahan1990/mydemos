# Generated by Django 3.2.9 on 2022-01-05 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0012_auto_20220105_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ak',
            name='status',
            field=models.CharField(blank=True, choices=[(1, 'Published'), (2, 'Unpublished'), (3, 'Reported')], default=1, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='ap',
            name='status',
            field=models.CharField(blank=True, choices=[(1, 'Published'), (2, 'Unpublished'), (3, 'Reported')], default=1, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='pf',
            name='status',
            field=models.CharField(blank=True, choices=[(1, 'Published'), (2, 'Unpublished'), (3, 'Reported')], default=1, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='pfw',
            name='status',
            field=models.CharField(blank=True, choices=[(1, 'Published'), (2, 'Unpublished'), (3, 'Reported')], default=1, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='phw',
            name='status',
            field=models.CharField(blank=True, choices=[(1, 'Published'), (2, 'Unpublished'), (3, 'Reported')], default=1, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='pim',
            name='status',
            field=models.CharField(blank=True, choices=[(1, 'Published'), (2, 'Unpublished'), (3, 'Reported')], default=1, max_length=2, null=True),
        ),
    ]
