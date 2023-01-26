# Generated by Django 4.1.5 on 2023-01-25 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ModelUpload",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tipo", models.CharField(max_length=4)),
                ("data", models.DateField()),
                ("valor", models.DecimalField(decimal_places=2, max_digits=8)),
                ("cpf", models.IntegerField()),
                ("cartao", models.IntegerField()),
                ("hora", models.DateTimeField(auto_now_add=True)),
                ("dono_da_loja", models.CharField(max_length=50)),
                ("nome_da_loja", models.CharField(max_length=50)),
            ],
        ),
    ]
