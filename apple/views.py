from django.shortcuts import render
from .models import students
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from .serilizer import student_serilise
from .my_pagenation import my_pagenation,my_limit_offset,my_curser_pagenation

# Create your views here.

def show(request):
    return render(request,'index.html')

class data(viewsets.ModelViewSet):
    queryset = students.objects.all()
    serializer_class = student_serilise
    pagination_class = my_pagenation
    # pagination_class = my_limit_offset

class data1(ListAPIView):
    queryset = students.objects.all()
    serializer_class = student_serilise
    pagination_class = my_limit_offset

class data2(ListAPIView):
    queryset = students.objects.all()
    serializer_class = student_serilise
    pagination_class = my_curser_pagenation