# Generated by Django 2.1.3 on 2018-11-12 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.CharField(blank=True, default='', max_length=50),
            preserve_default=False,
        ),
    ]
