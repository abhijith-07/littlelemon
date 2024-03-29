# Generated by Django 5.0.3 on 2024-03-16 14:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0002_alter_booking_inventory_alter_booking_price_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="booking",
            old_name="title",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="booking",
            old_name="inventory",
            new_name="no_of_guests",
        ),
        migrations.RenameField(
            model_name="menu",
            old_name="no_of_guests",
            new_name="inventory",
        ),
        migrations.RenameField(
            model_name="menu",
            old_name="name",
            new_name="title",
        ),
        migrations.RemoveField(
            model_name="booking",
            name="price",
        ),
        migrations.RemoveField(
            model_name="menu",
            name="bookingDate",
        ),
        migrations.AddField(
            model_name="booking",
            name="bookingDate",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="menu",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
