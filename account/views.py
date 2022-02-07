from html5lib import serialize
from account.models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import status 
from django.db import Q 
from account.serializers import *
import random
from send_otp import *
class UserRegistration(APIView):
     
    def post(self,request,*args,**kwargs):
        data=request.data
        generated_otp = random.randint(1000,9999)
        phone=data['phone_number']
        if len(phone)>10 or len(phone)<10:
        
            return Response({"message":"Phone number should 10 digit"},status=status.HTTP_406_NOT_ACCEPTABLE)
        
        elif phone.isdigit()==False:
            
            return Response({"message":"phone number should digit"},status=status.HTTP_406_NOT_ACCEPTABLE)
        
        serializers=RegistrationSerializers(data=data)
        if serializers .is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response()

        
        
       
