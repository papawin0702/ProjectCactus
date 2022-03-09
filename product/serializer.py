from rest_framework.serializers import ModelSerializer

from product.models import Category, Product, SubCategory

class CategorySerializer(ModelSerializer) :
    class Meta :
        model = Category
        fields = '__all__'

class SubCategorySerializer(ModelSerializer) :
    category = CategorySerializer(read_only=True)
    class Meta :
        model = SubCategory
        fields = '__all__'

    def get_category_name(self,obj):
        return obj.category.nsme


class ProductSerializer(ModelSerializer):
    category = SubCategorySerializer(read_only=True,many=True)
    class Meta :
        model = Product
        fields = '__all__'
