from rest_framework import serializers

from .models import *

class CategoriesSerializers(serializers.ModelSerializer):
    category_img_url = serializers.SerializerMethodField()

    class Meta:
        model = CategoriesModel
        fields = '__all__'

    def get_category_img_url(self, obj):
        request = self.context.get('request')
        if obj.category_img:
            image_url = obj.category_img.url
            return request.build_absolute_uri(image_url)
        return None
            

class BrandsSerializers(serializers.ModelSerializer):
    class Meta:
        model = BrandsModel
        fields = '__all__'

class ProductsSerializers(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category_ID.category_name', read_only=True)
    brand_name = serializers.CharField(source = 'brand_ID.brand_name', read_only = True)
    class Meta:
        model = ProductsModel
        #fields = '__all__'
        fields = [
            'product_name',
            'shortDes',
            'price',
            'discount',
            'discountPrice',
            'image',
            'star',
            'stock',
            'remark',
            'category_ID',
            'brand_ID',
            'created_at',
            'updated_at',
            'brand_name',
            'category_name'
        ]


class ProductsDetailsSerializers(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product_ID.product_name', read_only=True)
    class Meta:
        model = ProductsDetailsModel
        #fields = '__all__'
        fields = ['img1', 'img2', 'img3', 'description', 'color', 'size', 'product_ID', 'product_name']