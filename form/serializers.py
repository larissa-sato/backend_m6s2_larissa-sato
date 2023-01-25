from rest_framework import serializers
from .models import ModelUpload

class FormSerializer(serializers.Serializer):
    class Meta:
        model = ModelUpload
        fields = "__all__"