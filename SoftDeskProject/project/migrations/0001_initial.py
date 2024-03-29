# Generated by Django 4.0.4 on 2022-07-19 13:48

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
            name='Project',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )
                 ),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=20)),
                ('author_user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL
                )
                 ),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=250)),
                ('tag', models.CharField(max_length=50)),
                ('priority', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('assignee_user', models.ForeignKey(
                    blank=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='assignee',
                    to=settings.AUTH_USER_MODEL
                )
                 ),
                (
                    'author_user',
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='author_issue',
                        to=settings.AUTH_USER_MODEL
                    )
                ),
                (
                    'project', models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='issues',
                        to='project.project'
                    )
                ),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )
                 ),
                ('permission', models.CharField(
                    choices=[
                        ('R', 'read'),
                        ('RW', 'Read_Write'),
                        ('RWD', 'Read_Write_Delete')],
                    max_length=50
                )
                 ),
                (
                    'role',
                    models.CharField(
                        choices=[
                            ('ad', 'admin'),
                            ('te', 'technicien'),
                            ('cu', 'customer')
                        ],
                        max_length=20
                    )
                ),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')
                 ),
                ('description', models.CharField(max_length=250)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('author_user', models.ForeignKey(
                    blank=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='author_comment',
                    to=settings.AUTH_USER_MODEL
                )),
                ('issue', models.ForeignKey(
                    blank=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='issue',
                    to='project.issue'
                )),
            ],
        ),
    ]
