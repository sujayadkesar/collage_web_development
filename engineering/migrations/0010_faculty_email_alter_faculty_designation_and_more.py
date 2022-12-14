# Generated by Django 4.0.3 on 2022-12-01 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineering', '0009_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='Email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='faculty',
            name='Designation',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='Industry_Experience',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='Research_Experience',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='Teaching_Experience',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='description',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
