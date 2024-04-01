# Generated by Django 4.2.11 on 2024-04-01 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoticeTimes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.CharField(choices=[('ASAP', 'ASAP'), ('1 Week', '1 Week'), ('2 Weeks', '2 Weeks'), ('3 Weeks', '3 Weeks'), ('4 Week or more', '4 Weeks or more')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('cv', models.FileField(blank=True, upload_to='cv/')),
                ('address', models.CharField(blank=True, max_length=100)),
                ('notice', models.ManyToManyField(to='jobs.noticetimes')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
