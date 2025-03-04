# Generated by Django 2.2.7 on 2020-11-11 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('ratings', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.FileField(null=True, upload_to='Poster_Pics/')),
                ('movieId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Poster.Movies')),
            ],
        ),
    ]
