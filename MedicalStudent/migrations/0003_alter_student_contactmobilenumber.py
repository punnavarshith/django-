# Generated by Django 5.1.2 on 2024-11-28 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalStudent', '0002_alter_student_studentregnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='ContactMobileNumber',
            field=models.CharField(max_length=10),
        ),
    ]
