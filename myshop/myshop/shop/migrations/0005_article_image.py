# Generated by Django 4.2.1 on 2023-09-22 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='swiss_chocolate.png', upload_to='article_images/'),
            preserve_default=False,
        ),
    ]
