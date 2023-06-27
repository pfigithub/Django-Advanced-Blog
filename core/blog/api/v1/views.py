from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from .permissions import IsOwnerOrReadOnly
from .paginations import CustomDefaultPagination


# class base model_viewset
class PostModelViewSet(viewsets.ModelViewSet):
    """Model ViewSet for listing or retrieving posts and ..."""

    queryset = Post.objects.filter(status=True)
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    pagination_class = CustomDefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["category", "author"]
    search_fields = ["title", "content", "category__name"]
    ordering_fields = ["published_date"]


# # class base viewset view
# class PostViewSet(viewsets.ViewSet):
#     """A simple ViewSet for listing or retrieving posts"""

#     queryset = Post.objects.filter(status=True)
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer

#     def list(self, request):
#         serializer = self.serializer_class(self.queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         post_object = get_object_or_404(self.queryset, pk=pk)
#         serializer = self.serializer_class(post_object)
#         return Response(serializer.data)

#     def create(self, request):
#         pass

#     def update(self, request, pk=None):
#         pass

#     def partial_update(self, request, pk=None):
#         pass

#     def destroy(self, request, pk=None):
#         pass


# # class base generics view(post_list)
# class PostList(ListCreateAPIView):
#     """getting a list of posts and creating a post"""
#     queryset = Post.objects.filter(status=True)
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer


# # class base generics view(post_detail)
# class PostDetail(RetrieveUpdateDestroyAPIView):
#     """getting a detail of post,edit and delete a post"""
#     queryset = Post.objects.filter(status=True)
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer


# # class base api view(post_list)
# class PostList(APIView):
#     """getting a list of posts and creating a post"""

#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     def get(self, request):
#         """retriveing a list of posts"""

#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializer(posts, many=True )
#         return Response(serializer.data)

#     def post(self, request):
#         """creating a post with provided data"""

#         serializer = PostSerializer(data = request.data)
#         serializer.is_valid(raise_exception= True)
#         serializer.save()
#         return Response(serializer.data)


# # class base api view(post_detail)

# class PostDetail(APIView):
#     """getting a detail of post,edit and delete a post"""

#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer

#     def get(self, request, id):
#         """retriveing the post data"""
#         post = get_object_or_404(Post,pk=id,status = True)
#         serializer = self.serializer_class(post)
#         return Response(serializer.data)

#     def put(self, request, id):
#         """editing the post data"""
#         post = get_object_or_404(Post,pk=id,status = True)
#         serializer = PostSerializer(post,data = request.data)
#         serializer.is_valid(raise_exception= True)
#         serializer.save()
#         return Response(serializer.data)

#     def delete(self, request, id):
#         """deleting the post data"""
#         post = get_object_or_404(Post,pk=id,status = True)
#         post.delete()
#         return Response({'detail':'post removed successfully'},status = status.HTTP_204_NO_CONTENT)


# # function base api view(post_list)
# @api_view(['GET','POST'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def postList(request):
# """getting a list of posts and creating a post"""
#     if request.method == 'GET':
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializer(posts, many=True )
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PostSerializer(data = request.data)
#         serializer.is_valid(raise_exception= True)
#         serializer.save()
#         return Response(serializer.data)


# # function base api view(post_detail)
# @api_view(['GET','PUT','DELETE'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def postDetail(request, id):
#     if request.method == 'GET':
#         post = Post.objects.get(pk=id, status=True)
#         try:
#             serializer = PostSerializer(post)
#             return Response(serializer.data)
#         except Post.DoesNotExist:
#             return Response({'detail':'post does not exist'},status = status.HTTP_404_NOT_FOUND)
#     elif request.method == "PUT":
#         serializer = PostSerializer(post,data = request.data)
#         serializer.is_valid(raise_exception= True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == "DELETE":
#         serializer.delete()
#         return Response({'detail':'post removed successfully'},status = status.HTTP_204_NO_CONTENT )

# # or we can do that(postDetal) like this not diffrence but it is shorter

# # from django.shortcuts import get_object_or_404

# # @api_view()
# # def postDetail(request, id):
# #         post = get_object_or_404(Post,pk=id)
# #         serializer = PostSerializer(post)
# #         return Response(serializer.data)


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
