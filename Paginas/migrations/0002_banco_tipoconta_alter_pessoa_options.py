# Generated by Django 4.0.3 on 2022-05-09 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paginas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('codigo', models.DecimalField(decimal_places=0, max_digits=9999)),
            ],
        ),
        migrations.CreateModel(
            name='TipoConta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sigla', models.CharField(max_length=2)),
            ],
        ),
        migrations.AlterModelOptions(
            name='pessoa',
            options={'ordering': ['nome_completo']},
        ),
    ]