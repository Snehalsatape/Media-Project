# Generated by Django 5.0.6 on 2024-06-10 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('Audio', 'Audio'), ('Video', 'Video'), ('Image', 'Image')], max_length=5)),
                ('format', models.CharField(max_length=50)),
                ('size', models.FloatField()),
                ('duration_secs', models.IntegerField(default=0)),
            ],
        ),
    ]