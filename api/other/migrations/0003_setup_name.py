# Generated by Django 3.2.20 on 2024-05-13 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0002_alter_post_id_alter_session_id_alter_setup_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='setup',
            name='name',
            field=models.CharField(default='default name', max_length=50),
            preserve_default=False,
        ),
    ]
