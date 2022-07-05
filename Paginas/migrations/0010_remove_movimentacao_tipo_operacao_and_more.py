# Generated by Django 4.0.4 on 2022-07-05 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paginas', '0009_rename_data_e_hora_movimentacao_cadastrado_em_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimentacao',
            name='tipo_operacao',
        ),
        migrations.RemoveField(
            model_name='movimentacao',
            name='usuario',
        ),
        migrations.AddField(
            model_name='categoria',
            name='tipo_movimetacao',
            field=models.CharField(choices=[('E', 'Entrada'), ('S', 'Saída')], default='E', max_length=2),
        ),
        migrations.DeleteModel(
            name='TipoOperacao',
        ),
    ]
