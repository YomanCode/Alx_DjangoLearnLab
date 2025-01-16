from django.utils import timezone
from rest_framework import serializers
from .models import Task
from datetime import datetime

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_due_date(self, value):
        now = timezone.now()
        if isinstance(value, datetime):
            if value < now:
                raise serializers.ValidationError("Due date must be in the future")
        else:
            if value < now.date():
                raise serializers.ValidationError("Due date must be in the future")
        return value
