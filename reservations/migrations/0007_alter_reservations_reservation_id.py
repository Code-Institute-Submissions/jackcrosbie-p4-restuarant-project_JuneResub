# Generated by Django 3.2 on 2022-02-08 03:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0006_auto_20220208_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='reservation_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
