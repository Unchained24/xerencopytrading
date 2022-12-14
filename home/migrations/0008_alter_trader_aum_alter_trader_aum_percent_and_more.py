# Generated by Django 4.1.2 on 2022-10-13 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_trader_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trader',
            name='aum',
            field=models.DecimalField(blank=True, decimal_places=10, default=0.0, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='trader',
            name='aum_percent',
            field=models.DecimalField(blank=True, decimal_places=10, default=0.0, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='trader',
            name='drawdown_percent',
            field=models.DecimalField(blank=True, decimal_places=10, default=0.0, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='trader',
            name='profit',
            field=models.DecimalField(blank=True, decimal_places=10, default=0.0, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='trader',
            name='roiprofit',
            field=models.DecimalField(blank=True, decimal_places=10, default=0.0, max_digits=19, null=True),
        ),
    ]
