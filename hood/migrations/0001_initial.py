# Generated by Django 3.2.9 on 2022-01-04 20:23

import cloudinary.models
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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('occupants_count', models.IntegerField()),
                ('created', models.DateField(auto_now_add=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image')),
                ('Admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('user_name', models.CharField(max_length=255, null=True)),
                ('bio', models.CharField(max_length=255, null=True)),
                ('website_url', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.TextField()),
                ('twitter_url', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram_url', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook_url', models.CharField(blank=True, max_length=255, null=True)),
                ('neighbourhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='hood.neighbourhood')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image')),
                ('created', models.DateField(auto_now_add=True)),
                ('comments', models.CharField(blank=True, max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('neighbourhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.neighbourhood')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('created', models.DateField(auto_now_add=True)),
                ('neighbourhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.neighbourhood')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
