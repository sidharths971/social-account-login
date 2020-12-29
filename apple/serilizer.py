from  rest_framework import serializers
from .models import students

class student_serilise(serializers.ModelSerializer):

    class Meta:
        model = students
        fields = '__all__'