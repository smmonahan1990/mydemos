# Generated by Django 3.2.9 on 2022-01-05 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0009_report_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ak',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ak',
            name='json',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ak',
            name='score',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='ak',
            name='submitted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ak',
            name='title',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='ap',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ap',
            name='json',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ap',
            name='score',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='ap',
            name='submitted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ap',
            name='title',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='pf',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pf',
            name='json',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pf',
            name='score',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='pf',
            name='submitted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pf',
            name='title',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='pfw',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pfw',
            name='json',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pfw',
            name='score',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='pfw',
            name='submitted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pfw',
            name='title',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='phw',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='phw',
            name='json',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='phw',
            name='score',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='phw',
            name='submitted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='phw',
            name='title',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
    ]
