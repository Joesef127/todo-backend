# Generated by Django 5.1.4 on 2025-01-05 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('due_date', models.DateField()),
                ('priority', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
