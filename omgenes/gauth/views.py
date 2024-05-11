from django.shortcuts import render
from google.oauth2 import id_token
from google.auth.transport import requests
from django.conf import settings
from django.http import JsonResponse
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import authentication_classes, permission_classes

import logging
logger = logging.getLogger(__name__)


# Create your views here.

@authentication_classes([])
@permission_classes([])
@csrf_exempt
def verify_google_token(request):
    try:
        token = request.POST.get("id_token")
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), settings.GOOGLE_CLIENT_ID, clock_skew_in_seconds=3)
        user_id = idinfo['sub']
        logger.info(idinfo)
    
        return JsonResponse({"success": True, "user_id": user_id})
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})