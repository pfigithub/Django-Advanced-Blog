from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from rest_framework import status


@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def postList(request):
    if request.method == 'GET':
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True )
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data = request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data)
    


@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def postDetail(request, id):
    if request.method == 'GET':
        post = Post.objects.get(pk=id, status=True)
        try:
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response({'detail':'post does not exist'},status = status.HTTP_404_NOT_FOUND)
    elif request.method == "PUT":
        serializer = PostSerializer(post,data = request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        serializer.delete()
        return Response({'detail':'post removed successfully'},status = status.HTTP_204_NO_CONTENT )

# or we can do that(postDetal) like this not diffrence but it is shorter

# from django.shortcuts import get_object_or_404

# @api_view()
# def postDetail(request, id):
#         post = get_object_or_404(Post,pk=id)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)