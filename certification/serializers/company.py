from rest_framework import serializers
from certification.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'description',
            'creation_date',
            'persons',
            'github_organization_name',
            'linkedin_vanity_name',
            'created_at',
            'updated_at',
        )
