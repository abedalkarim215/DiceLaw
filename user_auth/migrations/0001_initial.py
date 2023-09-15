# Generated by Django 4.2.5 on 2023-09-13 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attorney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('about', models.TextField()),
                ('image', models.ImageField(upload_to='attorney_images/')),
                ('practice_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.practicearea')),
            ],
        ),
    ]
