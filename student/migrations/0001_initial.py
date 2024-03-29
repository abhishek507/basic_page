# Generated by Django 4.0.3 on 2024-02-29 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stu_id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('stu_name', models.CharField(max_length=100, null=True)),
                ('stu_age', models.IntegerField()),
                ('stu_dept', models.CharField(choices=[('cse', 'CSE'), ('mech', 'MECH'), ('ece', 'ECE'), ('eee', 'EEE')], max_length=50)),
                ('stu_gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE')], max_length=20)),
            ],
            options={
                'db_table': 'Student',
            },
        ),
    ]
