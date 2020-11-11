# Generated by Django 3.1.2 on 2020-11-10 20:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simulatorApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consistency', models.DecimalField(decimal_places=4, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaderboard_position', models.IntegerField(default=-1)),
                ('school_position', models.IntegerField(default=-1)),
                ('schoolid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulatorApp.school')),
                ('strategyid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='simulatorApp.strategy')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('is_team', 'Is a team account'),),
            },
        ),
    ]