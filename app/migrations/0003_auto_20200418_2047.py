# Generated by Django 3.0.5 on 2020-04-18 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200418_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='Fare',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='passenger',
            name='Parch',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='passenger',
            name='Pclass',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='passenger',
            name='SibSp',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='passenger',
            name='cabin',
            field=models.CharField(default=1, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='passenger',
            name='embarked',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='passenger',
            name='sex',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='passenger',
            name='ticket',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='passenger',
            name='title',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='passenger',
            name='age',
            field=models.IntegerField(),
        ),
    ]
