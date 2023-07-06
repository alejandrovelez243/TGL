from rest_framework import viewsets
from film.models import Film
from .serializers import FilmSerializer
from rest_framework import generics
# Create your views here.


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer



class FilmGeneric(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def get_queryset(self):
        queryset = super(FilmGeneric, self).get_queryset()
        user = self.request.user
        if not self.request.user.is_superuser:
            queryset.objects.filter(estado=True)
        return queryset


    def get(self, request, *args, **kwargs):
        """Prueba de documentación

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        print("Hola entre al get")
        return super(FilmGeneric, self).get(request, *args, **kwargs)



class FilmGenericDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def retrieve(self, request, *args, **kwargs):
        print("Soy retrieve")
        return super(FilmGenericDetail, self).retrieve(request, *args, **kwargs)
