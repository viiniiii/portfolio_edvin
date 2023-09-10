from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name=None)),
                ('title', models.CharField(max_length=75)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='portfolio/images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]