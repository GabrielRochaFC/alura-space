# Generated by Django 4.2.4 on 2023-09-11 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('GALÁXIA', 'Galáxia'), ('NEBULOSA', 'Nebulosa'), ('ESTRELA', 'Estrela'), ('PLANETA', 'Planeta')], default='', max_length=100),
        ),
    ]
