# Generated by Django 4.1.7 on 2023-02-23 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_internship'),
    ]

    operations = [
        migrations.CreateModel(
            name='intern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internship_name', models.CharField(max_length=122)),
                ('company_name', models.CharField(max_length=122)),
                ('location', models.CharField(max_length=122)),
                ('CTC', models.CharField(max_length=122)),
                ('type', models.CharField(max_length=122)),
                ('apply_link', models.CharField(max_length=122)),
            ],
        ),
        migrations.DeleteModel(
            name='internships',
        ),
    ]