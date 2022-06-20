# Generated by Django 4.0.4 on 2022-06-20 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Paginas', '0006_tipoconta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=0, max_digits=50)),
                ('data_e_hora', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Paginas.categoria')),
                ('tipo_operacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Paginas.tipooperacao', verbose_name='Tipo Operação')),
            ],
        ),
    ]
