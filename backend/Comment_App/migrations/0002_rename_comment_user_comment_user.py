# Generated by Django 4.0.4 on 2022-05-12 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Comment_App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_user',
            new_name='user',
        ),
    ]