from rest_framework import viewsets

# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
