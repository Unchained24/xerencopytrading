# Generated by Django 4.1.2 on 2022-10-13 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_trader_aum_alter_trader_aum_percent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='featured_image',
            field=models.ImageField(blank=True, default='assets/img/uploads/default.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='trader',
            name='aum',
            field=models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='trader',
            name='aum_percent',
            field=models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='trader',
            name='cover_photo',
            field=models.ImageField(blank=True, default='assets/img/default.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='trader',
            name='drawdown_percent',
            field=models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='trader',
            name='profit',
            field=models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='trader',
            name='roiprofit',
            field=models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=19, null=True),
        ),
    ]
