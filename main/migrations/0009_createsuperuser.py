import os
from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('main', '0008_post_tags_delete_posttags'),
    ] # can also be emtpy if it's your first migration

    def generate_superuser(apps, schema_editor):
        from main.models import User

        superuser = User.objects.create_superuser(
            username='admin',
            email='',
            password='admin')

        superuser.save()

    operations = [
        migrations.RunPython(generate_superuser),
    ]