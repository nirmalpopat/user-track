# Generated by Django 4.0.6 on 2022-07-29 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0002_alter_history_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]