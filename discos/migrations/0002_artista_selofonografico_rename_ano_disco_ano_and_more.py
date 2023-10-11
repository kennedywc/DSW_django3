# Generated by Django 4.2.6 on 2023-10-11 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artista', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SeloFonografico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selo_fonografico', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='disco',
            old_name='Ano',
            new_name='ano',
        ),
        migrations.RenameField(
            model_name='disco',
            old_name='Descricao',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='disco',
            old_name='Genero',
            new_name='genero',
        ),
        migrations.RenameField(
            model_name='disco',
            old_name='Nome',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='disco',
            old_name='Pais',
            new_name='pais',
        ),
        migrations.RenameField(
            model_name='disco',
            old_name='Quantidade',
            new_name='quantidade',
        ),
        migrations.RemoveField(
            model_name='disco',
            name='Selo_fonografico',
        ),
        migrations.AddField(
            model_name='disco',
            name='artista',
            field=models.ManyToManyField(to='discos.artista'),
        ),
        migrations.AddField(
            model_name='disco',
            name='selo_fonografico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='discos.selofonografico'),
        ),
    ]
