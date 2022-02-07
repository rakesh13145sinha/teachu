from attr import field
from rest_framework import serializers 
from account.models import Registration 
class RegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model=Registration 
        fields='__all__'