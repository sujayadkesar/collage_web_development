# Generated by Django 4.0.3 on 2022-11-22 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_profile_usn'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='USN_Number',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
