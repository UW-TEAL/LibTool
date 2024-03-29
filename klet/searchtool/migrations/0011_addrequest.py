# Generated by Django 4.1.7 on 2023-05-05 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchtool', '0010_record_uid2'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestid', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('accepted', models.BooleanField(default=False)),
                ('authorKorean', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('authorEnglish', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('workTitle', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('genre', models.CharField(blank=True, choices=[('Fictions', 'Fictions'), ('Poems', 'Poems'), ('Essays', 'Essays'), ('Plays', 'Plays'), ('Childrens', 'Childrens'), ('Classic_General', 'Classic_General'), ('Classic_Poem', 'Classic_Poem'), ('Classic_History', 'Classic_History'), ('Classic_Folk Tale', 'Classic_Folk Tale'), ('Classic_Fiction', 'Classic_Fiction'), ('Misc', 'Misc')], default=('Poems', 'Poems'), max_length=200, null=True)),
                ('translator', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('sourceTitle', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('publisher', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('year', models.CharField(blank=True, default=' ', max_length=100, null=True)),
                ('yearCreated', models.FloatField(blank=True, default=0.0, null=True)),
                ('authorEnglish2', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('uid2', models.CharField(default='Not Registered yet', max_length=100)),
                ('other', models.CharField(blank=True, default='', max_length=300, null=True)),
            ],
        ),
    ]
