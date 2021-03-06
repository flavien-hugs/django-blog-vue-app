# Generated by Django 4.0.1 on 2022-01-09 07:21

import common.utilitary
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='uuid')),
                ('slug', models.SlugField(blank=True, editable=False, help_text='Automatiquement formé à partir du nom.', null=True, unique=True, unique_for_date='created_at', verbose_name='slug')),
                ('name', models.CharField(blank=True, default='Non définie', help_text="Définir le type de catégorie de l'article.", max_length=120, null=True, unique=True, verbose_name="type de catégorie d'article")),
                ('image', models.ImageField(blank=True, help_text="ajouter une image descriptive de l'article.", null=True, upload_to=common.utilitary.img_url, verbose_name='ajouter une image')),
            ],
            options={
                'verbose_name_plural': 'catégories',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='uuid')),
                ('slug', models.SlugField(blank=True, editable=False, help_text='Automatiquement formé à partir du nom.', null=True, unique=True, unique_for_date='created_at', verbose_name='slug')),
                ('name', models.CharField(help_text="Définir le titre de l'article.", max_length=255, unique=True, verbose_name="titre de l'article")),
                ('subtitle', models.CharField(blank=True, help_text="Définir un sous-titre de l'article.", max_length=255, null=True, verbose_name='sous-titre')),
                ('body', models.TextField(help_text="Éditer le contenu de l'article.", verbose_name="Contenu de l'article")),
                ('image', models.ImageField(blank=True, help_text="ajouter une image descriptive de l'article.", null=True, upload_to=common.utilitary.img_url, verbose_name='ajouter une image')),
                ('view', models.PositiveIntegerField(default=0, editable=False, verbose_name='nombre de vues')),
                ('status', models.CharField(choices=[('Publié', 'Publié'), ('Brouillon', 'Brouillon'), ('Relecture', 'Relecture')], default='Brouillon', help_text="définir le status de l'article.", max_length=10, verbose_name='status')),
                ('published', models.DateTimeField(help_text="Programmé la date et l'heure de publication", verbose_name='date et de publication')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category', verbose_name='catégorie')),
            ],
            options={
                'verbose_name_plural': 'articles',
                'ordering': ['-published'],
                'get_latest_by': ['-published'],
            },
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['uuid'], name='blog_catego_uuid_ced970_idx'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['uuid'], name='blog_post_uuid_a20c8f_idx'),
        ),
    ]
