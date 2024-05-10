from django.shortcuts import render
from google.oauth2 import id_token
from google.auth.transport import requests
from django.conf import settings
from django.http import JsonResponse
# Create your views here.

def verify_google_token(request):
    token = request.POST.get("id_token")
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), settings.GOOGLE_CLIENT_ID)
        user_id = idinfo['sub']

        return JsonResponse({"success": True, "user_id": user_id})
    except Execption as e:
        return JsonResponse({"success": False, "user_id": str(e)})