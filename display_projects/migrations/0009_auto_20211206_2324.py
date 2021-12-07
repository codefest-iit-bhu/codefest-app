# Generated by Django 2.1.5 on 2021-12-06 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('display_projects', '0008_auto_20211206_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('likes_count', models.PositiveIntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('commentor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='CommentRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rated_comment', to='display_projects.Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='projectcomment',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projectcomment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='projectrating',
            name='rating',
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='likes_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='views_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projectrating',
            name='like',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectrating',
            name='view',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='ProjectComment',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='display_projects.ProjectModel'),
        ),
        migrations.AlterUniqueTogether(
            name='commentrating',
            unique_together={('user', 'comment')},
        ),
    ]
