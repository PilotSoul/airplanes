# Generated by Django 4.2.6 on 2023-10-29 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='plane',
        ),
        migrations.AddField(
            model_name='customuser',
            name='plane',
            field=models.ManyToManyField(null=True, to='user_profile.plane'),
        ),
    ]