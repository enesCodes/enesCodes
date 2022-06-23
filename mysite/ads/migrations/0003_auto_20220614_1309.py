# Generated by Django 3.2.5 on 2022-06-14 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_auto_20220613_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='pic',
        ),
        migrations.AddField(
            model_name='ad',
            name='content_type',
            field=models.CharField(blank=True, help_text='The MIMEType of the file', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='ad',
            name='picture',
            field=models.BinaryField(blank=True, editable=True, null=True),
        ),
        migrations.DeleteModel(
            name='Pic',
        ),
    ]
