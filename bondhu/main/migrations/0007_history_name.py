# Generated by Django 3.2.9 on 2021-12-09 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_history_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
