# Generated by Django 4.1.2 on 2022-12-02 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
