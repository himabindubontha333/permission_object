from django.shortcuts import render
from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from .permissions import IsEditorOrReadOnly, IsAdminOrReadOnly, IsViewer, IsCreatorOrReadOnly

# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrReadOnly]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update']:
            permission_classes = [IsEditorOrReadOnly]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [IsViewer]
        else:
            permission_classes = [IsCreatorOrReadOnly]
        return [permission() for permission in permission_classes]

