# Generated by Django 2.2.10 on 2021-03-28 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('answer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='interview_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='answer.InterviewUser'),
        ),
    ]