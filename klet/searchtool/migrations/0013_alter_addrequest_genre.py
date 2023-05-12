# Generated by Django 4.1.7 on 2023-05-12 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchtool', '0012_record_worktitlekorean'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addrequest',
            name='genre',
            field=models.CharField(blank=True, choices=[('Fiction', 'Fiction'), ('Poetry', 'Poetry'), ('Essay', 'Essay'), ('Play', 'Play'), ('Children’s Literature', 'Children’s Literature'), ('Classic_General', 'Classic_General'), ('Classic_Poetry', 'Classic_Poetry'), ('Classic_History', 'Classic_History'), ('Classic_Folk Tale', 'Classic_Folk Tale'), ('Classic_Fiction', 'Classic_Fiction'), ('Misc', 'Misc')], default=('Poetry', 'Poetry'), max_length=200, null=True),
        ),
    ]