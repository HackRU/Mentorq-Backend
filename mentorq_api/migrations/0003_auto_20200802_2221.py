# Generated by Django 3.0.8 on 2020-08-02 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorq_api', '0002_feedback'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'Feedback', 'verbose_name_plural': 'Feedback'},
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('OPEN', 'Open'), ('CLOSED', 'Closed'), ('CLAIMED', 'Claimed'), ('CANCELLED', 'Cancelled')], default='OPEN', max_length=9),
        ),
    ]