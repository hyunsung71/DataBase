# Generated by Django 2.2.5 on 2020-11-21 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0009_auto_20201121_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedday',
            name='roomtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.RoomType'),
        ),
    ]
