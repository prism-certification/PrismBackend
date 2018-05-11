from rest_framework import serializers
from certification.models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = (
            'id',
            'description',
            'field',
            'created_at',
            'updated_at',
        )
