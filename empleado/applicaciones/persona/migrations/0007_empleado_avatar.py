# Generated by Django 2.1.15 on 2020-05-25 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0006_empleado_hoja_vida'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
    ]