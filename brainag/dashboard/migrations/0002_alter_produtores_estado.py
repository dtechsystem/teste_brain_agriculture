# Generated by Django 5.0.9 on 2024-10-07 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtores',
            name='estado',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
