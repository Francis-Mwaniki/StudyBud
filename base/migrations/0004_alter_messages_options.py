# Generated by Django 4.1.4 on 2022-12-18 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_alter_room_options_room_participants"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="messages",
            options={"ordering": ["-updated", "-created"]},
        ),
    ]
