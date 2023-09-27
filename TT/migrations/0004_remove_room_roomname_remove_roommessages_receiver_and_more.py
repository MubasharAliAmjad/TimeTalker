# Generated by Django 4.2.5 on 2023-09-26 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TT', '0003_remove_room_roommembers_room_roommembers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='roomName',
        ),
        migrations.RemoveField(
            model_name='roommessages',
            name='receiver',
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default=0.0004970178926441351, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='room',
            name='roomMembers',
        ),
        migrations.AlterField(
            model_name='roommessages',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='TT.room'),
        ),
        migrations.AddField(
            model_name='room',
            name='roomMembers',
            field=models.ManyToManyField(related_name='rooms', to=settings.AUTH_USER_MODEL),
        ),
    ]
