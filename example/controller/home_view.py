from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import JsonResponse


class HomeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes =[IsAuthenticated]
    def get(self, request):
        content = {
            'user': str(request.user), 
        }
        return HttpResponse(JsonResponse({"status": "OK", "message":"sucesso", "user":content["user"]}), content_type="application/json", status=200)