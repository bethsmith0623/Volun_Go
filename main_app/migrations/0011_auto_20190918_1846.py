# Generated by Django 2.2.3 on 2019-09-18 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_event_attending'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='email',
            new_name='website',
        ),
    ]
