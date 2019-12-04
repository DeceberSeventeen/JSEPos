# Generated by Django 2.2 on 2019-04-24 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_order_price', models.FloatField()),
                ('be_given', models.FloatField()),
                ('give_change', models.FloatField()),
                ('order_datetime', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[(0, '付清'), (1, '挂单')], max_length=1)),
                ('paidOff_datetime', models.DateTimeField(auto_now_add=True)),
                ('print_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='goods.Goods')),
                ('order', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sale', to='sale.Order')),
            ],
        ),
    ]