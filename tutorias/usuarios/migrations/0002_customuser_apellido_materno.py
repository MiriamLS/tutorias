# Generated by Django 5.0.7 on 2024-07-28 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='apellido_materno',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]