# Generated by Django 4.1.3 on 2023-10-01 13:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("make_ktheme", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="uploadedimage",
            name="position_x",
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="uploadedimage",
            name="position_y",
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
