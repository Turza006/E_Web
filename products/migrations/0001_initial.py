# Generated by Django 2.0.2 on 2019-09-15 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('detail', models.TextField()),
                ('url', models.TextField()),
                ('view', models.IntegerField(default=1)),
                ('seller', models.TextField()),
                ('catagorys', models.ManyToManyField(to='products.Catagory')),
            ],
        ),
    ]
