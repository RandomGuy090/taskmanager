# Generated by Django 3.2 on 2021-07-15 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0012_alter_tables_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='tables',
            name='borderColor',
            field=models.CharField(default='#8CAE22', max_length=16),
        ),
    ]
