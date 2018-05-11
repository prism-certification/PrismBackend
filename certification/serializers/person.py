from rest_framework import serializers
from certification.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'id',
            'name',
            'nickname',
            'birthday',
            'github_user_name',
            'linkedin_vanity_name',
            'stackoverflow_id',
            'created_at',
            'updated_at',
        )
