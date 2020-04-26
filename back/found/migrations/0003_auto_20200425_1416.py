# Generated by Django 3.0.5 on 2020-04-25 05:16

from django.db import migrations, models
import django.db.models.deletion
import found.models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('found', '0002_foundimage_numpy_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foundimage',
            name='posting',
        ),
        migrations.RemoveField(
            model_name='foundimage',
            name='thumbnail',
        ),
        migrations.RemoveField(
            model_name='foundposting',
            name='has_img',
        ),
        migrations.AddField(
            model_name='foundimage',
            name='category_1',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='foundimage',
            name='category_2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='foundimage',
            name='category_3',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='foundposting',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='found.FoundImage'),
        ),
        migrations.CreateModel(
            name='FoundThumbnail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', imagekit.models.fields.ProcessedImageField(upload_to=found.models.thumbnail_path)),
                ('posting', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='found.FoundPosting')),
            ],
        ),
    ]