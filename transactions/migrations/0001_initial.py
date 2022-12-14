# Generated by Django 4.1.3 on 2022-11-25 14:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("type", models.CharField(max_length=1)),
                ("date", models.CharField(max_length=8)),
                ("value", models.IntegerField()),
                ("cpf", models.CharField(max_length=11)),
                ("card", models.CharField(max_length=12)),
                ("hour", models.CharField(max_length=6)),
                ("owner_shop", models.CharField(max_length=14)),
                ("shop", models.CharField(max_length=19)),
            ],
        ),
    ]
