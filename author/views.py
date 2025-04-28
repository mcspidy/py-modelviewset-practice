
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound
from author.models import Author
from author.serializers import AuthorSerializer
from django.shortcuts import get_object_or_404


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    def get_object(self):
        # Override get_object to handle 404 errors
        obj = get_object_or_404(self.queryset, pk=self.kwargs.get('pk'))
        if not obj:
            raise NotFound(detail="Author not found", code=404)
        return obj
