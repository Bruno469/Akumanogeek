# Generated by Django 5.0.4 on 2024-05-04 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0006_alter_produtos_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='imagem',
            field=models.ImageField(upload_to=''),
        ),
    ]
