# Generated by Django 5.0.3 on 2024-03-18 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summaries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='summarie',
            name='title',
            field=models.CharField(default='Nenhum título adicionado.', max_length=30),
        ),
    ]
