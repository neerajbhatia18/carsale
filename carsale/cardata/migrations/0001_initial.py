# Generated by Django 3.0.6 on 2020-08-03 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('v_id', models.IntegerField()),
                ('c_name', models.CharField(max_length=40)),
                ('c_mobile', models.TextField()),
                ('c_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(max_length=20)),
                ('a_cost', models.IntegerField()),
                ('chassis_no', models.CharField(max_length=30)),
                ('engine_no', models.CharField(max_length=30)),
                ('registered_address', models.TextField()),
                ('insurance', models.CharField(max_length=40)),
                ('insurance_date', models.DateTimeField()),
                ('v_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cardata.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Daily_Records',
            fields=[
                ('m_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cardata.Customer')),
            ],
        ),
    ]
