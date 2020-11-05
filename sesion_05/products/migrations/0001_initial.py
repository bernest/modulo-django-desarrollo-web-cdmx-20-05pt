# Generated by Django 3.1.3 on 2020-11-05 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, 'Muy malo'), (2, 'Malo'), (3, 'Regular'), (4, 'Bueno'), (5, 'Muy bueno')])),
            ],
        ),
    ]