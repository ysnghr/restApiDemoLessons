# Generated by Django 3.2.7 on 2021-09-03 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiller', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profil',
            options={'verbose_name_plural': 'Profiller'},
        ),
        migrations.AlterModelOptions(
            name='profildurum',
            options={'verbose_name_plural': 'Profil Mesajlari'},
        ),
        migrations.AlterField(
            model_name='profil',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='profil_fotolari/%Y/%m'),
        ),
    ]
