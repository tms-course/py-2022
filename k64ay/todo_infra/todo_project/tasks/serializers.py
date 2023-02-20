from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.Serializer):
    author = serializers.CurrentUserDefault()
    desc = serializers.CharFied(max_lenght=255)
    done = serializers.BooleanFiels()
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Task

#class TaskSerializer(ModelSerializer):
#    class Meta:
#        model = Task
#        fields = ['desc', 'author', 'created_at', 'done', 'id']
