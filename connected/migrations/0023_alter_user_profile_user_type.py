# Generated by Django 4.0.4 on 2022-06-05 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connected', '0022_remove_courses_educator_name_educator_profile_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='user_type',
            field=models.CharField(choices=[('learner', 'learner'), ('parent', 'parent')], default='learner', max_length=10),
        ),
    ]
