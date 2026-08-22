from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from escola.models import Estudante, Curso, Matricula
from escola.serializers import (
    EstudanteSerializer,
    CursoSerializer,
    MatriculaSerializer,
    MatriculasPorEstudanteSerializer,
    MatriculasPorCursoSerializer,
)


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculasPorEstudante(generics.ListAPIView):
    def get_queryset(self):  # type: ignore[override]
        queryset = Matricula.objects.filter(estudante_id=self.kwargs["pk"])
        return queryset

    serializer_class = MatriculasPorEstudanteSerializer


class MatriculasPorCurso(generics.ListAPIView):
    def get_queryset(self):  # type: ignore[override]
        queryset = Matricula.objects.filter(curso_id=self.kwargs["pk"])
        return queryset

    serializer_class = MatriculasPorCursoSerializer
