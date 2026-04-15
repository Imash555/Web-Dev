from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        source="category",
        queryset=Category.objects.all(),
        write_only=True,
        required=False,
    )

    class Meta:
        model = Product
        fields = '__all__'

    def validate(self, attrs):
        # For create requests, accept either category_id in payload.
        if self.instance is None and "category" not in attrs:
            raise serializers.ValidationError(
                {"category_id": ["This field is required."]}
            )
        return attrs