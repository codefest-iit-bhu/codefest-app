# Generated by Django 2.1.5 on 2021-12-03 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('screenshot', models.ImageField(upload_to='screenshots')),
                ('description', models.TextField(default='Enter the description here')),
                ('link', models.URLField(blank=True)),
                ('likes', models.PositiveSmallIntegerField(default=0)),
                ('dislikes', models.PositiveSmallIntegerField(default=0)),
                ('creator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
