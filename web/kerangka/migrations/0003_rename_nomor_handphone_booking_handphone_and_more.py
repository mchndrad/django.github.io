# Generated by Django 4.2.6 on 2024-01-03 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kerangka', '0002_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='nomor_handphone',
            new_name='handphone',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='nama_lengkap',
            new_name='nama',
        ),
        migrations.AlterField(
            model_name='booking',
            name='pemilihan_paket',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterModelTable(
            name='booking',
            table='booking',
        ),
    ]
