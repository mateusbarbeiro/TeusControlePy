# Generated by Django 4.0.4 on 2022-06-20 23:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Paginas', '0008_movimentacao_usuario_pessoa_cpf_pessoa_usuario_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movimentacao',
            old_name='data_e_hora',
            new_name='cadastrado_em',
        ),
        migrations.AddField(
            model_name='movimentacao',
            name='atualizado_em',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='contabancaria',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contabancaria',
            name='valor_total',
            field=models.DecimalField(decimal_places=0, max_digits=99999999999),
        ),
    ]