# Generated by Django 4.1.7 on 2023-02-24 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_interns_internship_ctc_internship_apply_link_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='interns',
        ),
        migrations.AddField(
            model_name='intern',
            name='duration',
            field=models.CharField(default='', max_length=122),
        ),
        migrations.AddField(
            model_name='intern',
            name='upload_duration',
            field=models.CharField(default='', max_length=122),
        ),
    ]
