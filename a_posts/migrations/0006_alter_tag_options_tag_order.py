# Generated by Django 5.1.2 on 2024-10-23 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_posts', '0005_tag_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='tag',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]
