# Generated by Django 3.2.9 on 2021-12-08 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211208_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.profiles'),
        ),
    ]
