# Generated by Django 5.2.1 on 2025-05-13 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_rename_contact_contact_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.AddField(
            model_name='contact',
            name='number',
            field=models.CharField(default=8737056329, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
