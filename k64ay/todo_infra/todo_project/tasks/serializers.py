from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task 
        fields = ['id', 'desc', 'done', 'created_at']


# class TaskSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.PrimaryKeyRelatedField(read_only=True)
#     desc = serializers.CharField()
#     done = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         return Task.objects.create(**validated_data)


#     def update(self, instance, validated_data):
#         instance.desc = validated_data.get('desc', instance.desc)
#         instance.done = validated_data.get('done', instance.done)
#         instance.save()

#         return instance