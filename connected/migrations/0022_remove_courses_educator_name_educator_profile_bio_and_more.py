# Generated by Django 4.0.4 on 2022-06-05 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connected', '0021_alter_courses_course_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='educator_name',
        ),
        migrations.AddField(
            model_name='educator_profile',
            name='bio',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='educator_profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/covers/'),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='bio',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Profile Picture'),
        ),
    ]
