# Generated by Django 5.0.4 on 2024-05-03 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0002_alter_produtos_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='tags',
            field=models.ManyToManyField(blank=True, to='HomePage.tag'),
        ),
    ]
