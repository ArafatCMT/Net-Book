# Generated by Django 5.1.2 on 2024-10-19 06:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(blank=True, default='https://i.ibb.co/XsJCM4t/image-placeholder-icon-11.png', max_length=250, null=True)),
                ('phone_no', models.CharField(blank=True, default='Phone  ', max_length=12, null=True)),
                ('city', models.CharField(blank=True, default='Address', max_length=30, null=True)),
                ('description', models.CharField(blank=True, default='Lorem ipsum dolor sit ame consectetur adipisicing elit. Quos eaque aliquam exceptur sed vitae. Nisi?', max_length=105, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='accounts.account')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='accounts.account')),
            ],
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_account', to='accounts.account')),
                ('sender_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_account', to='accounts.account')),
            ],
            options={
                'verbose_name_plural': 'Friends',
            },
        ),
    ]
