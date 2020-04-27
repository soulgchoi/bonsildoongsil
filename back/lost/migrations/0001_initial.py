# Generated by Django 3.0.5 on 2020-04-27 01:28

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import imagekit.models.fields
import lost.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('found', '0008_remove_foundposting_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='LostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=lost.models.lost_image_path)),
                ('category_1', models.CharField(blank=True, max_length=20)),
                ('category_2', models.CharField(blank=True, max_length=20)),
                ('category_3', models.CharField(blank=True, max_length=20)),
                ('numpy_path', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LostPosting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.BooleanField()),
                ('content', models.TextField()),
                ('lostname', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('do_notice', models.BooleanField()),
                ('lost_time', models.DateTimeField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='found.Category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='found.Color')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='LostThumbnail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=lost.models.lost_thumbnail_path)),
                ('posting', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thumbnail', to='lost.LostPosting')),
            ],
        ),
        migrations.CreateModel(
            name='LostAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_name', models.CharField(max_length=200)),
                ('region_1depth_name', models.CharField(max_length=50)),
                ('region_2depth_name', models.CharField(max_length=50)),
                ('region_3depth_name', models.CharField(max_length=50)),
                ('road_name', models.CharField(max_length=50)),
                ('zone_no', models.CharField(max_length=20)),
                ('x', models.CharField(max_length=50)),
                ('y', models.CharField(max_length=50)),
                ('lostposting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='lost.LostPosting')),
            ],
        ),
    ]