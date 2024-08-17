# Generated by Django 4.2.15 on 2024-08-16 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('macros', '0004_alter_goal_goal_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Standards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=20)),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('activity_level', models.CharField(choices=[(1.2, 'Inactive/Sedentary'), (1.375, 'Slightly Active'), (1.55, 'Moderately Active'), (1.7, 'Very Active'), (1.9, 'Extremely Active')], default=1.2, max_length=20)),
            ],
        ),
    ]
