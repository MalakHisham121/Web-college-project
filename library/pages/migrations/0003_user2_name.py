# Generated by Django 5.0.6 on 2024-08-24 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_user2_alter_borroweduser_user_id_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user2',
            name='name',
            field=models.CharField(default=99, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]