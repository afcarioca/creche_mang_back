
from rest_framework.views import APIView


class LoginView(APIView):
    def post(self, request):
        print(request)