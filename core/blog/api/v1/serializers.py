from rest_framework import serializers
from ...models import Post

# example for serializer
# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length =255 )

# example for model_serializer
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id','author','title','content','status','created_date','published_date']

