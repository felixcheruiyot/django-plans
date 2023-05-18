# Generated by Django 3.0.9 on 2020-08-03 13:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("plans", "0007_recurringuserplan_card_masked_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="recurringuserplan",
            name="token_verified",
            field=models.BooleanField(
                default=False,
                help_text="The recurring token has been verified by at least one payment to be working.",
                verbose_name="token has been verified by payment",
            ),
        ),
    ]
