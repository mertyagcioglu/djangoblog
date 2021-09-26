# Generated by Django 3.2.7 on 2021-09-24 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_content',
            field=models.CharField(default=1, max_length=200, verbose_name='Yorum'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_author',
            field=models.CharField(max_length=50, verbose_name='İsim'),
        ),
    ]
