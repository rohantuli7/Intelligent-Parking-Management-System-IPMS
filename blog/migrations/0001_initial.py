 # Generated by Django 3.0.2 on 2020-02-20 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=40)),
                ('altemail', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('repassword', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
                ('cp', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6)),
                ('contactno', models.CharField(max_length=10)),
            ],
        ),
    ]