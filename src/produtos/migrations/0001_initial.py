# Generated by Django 3.2.6 on 2021-09-13 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade', models.IntegerField()),
            ],
        ),
    ]
