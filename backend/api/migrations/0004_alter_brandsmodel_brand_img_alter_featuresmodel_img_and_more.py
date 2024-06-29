# Generated by Django 5.0.6 on 2024-06-29 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_categoriesmodel_category_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandsmodel',
            name='brand_img',
            field=models.ImageField(upload_to='images/brandImg/'),
        ),
        migrations.AlterField(
            model_name='featuresmodel',
            name='img',
            field=models.ImageField(upload_to='images/featureImg/'),
        ),
        migrations.AlterField(
            model_name='productsdetailsmodel',
            name='img1',
            field=models.ImageField(upload_to='images/productDetailImg/'),
        ),
        migrations.AlterField(
            model_name='productsdetailsmodel',
            name='img2',
            field=models.ImageField(upload_to='images/productDetailImg/'),
        ),
        migrations.AlterField(
            model_name='productsdetailsmodel',
            name='img3',
            field=models.ImageField(upload_to='images/productDetailImg/'),
        ),
        migrations.AlterField(
            model_name='productslidermodel',
            name='img',
            field=models.ImageField(upload_to='images/productSliderImg/'),
        ),
        migrations.AlterField(
            model_name='productsmodel',
            name='image',
            field=models.ImageField(upload_to='images/productImg/'),
        ),
    ]
