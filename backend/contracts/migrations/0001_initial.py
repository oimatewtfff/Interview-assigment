# Generated by Django 4.0.5 on 2022-06-18 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contracts',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('contract', models.IntegerField(null=True)),
                ('price_usd', models.IntegerField(null=True)),
                ('price_rub', models.IntegerField(null=True)),
                ('date', models.DateField(null=True)),
            ],
        ),
    ]
