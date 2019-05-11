# Generated by Django 2.2.1 on 2019-05-11 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customdashboard', '0001_initial'),
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='programnarratives',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workflow.Program'),
        ),
        migrations.AddField(
            model_name='programlinks',
            name='link',
            field=models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customdashboard.Link'),
        ),
        migrations.AddField(
            model_name='programlinks',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workflow.Program'),
        ),
        migrations.AddField(
            model_name='jupyternotebooks',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workflow.Program'),
        ),
    ]
