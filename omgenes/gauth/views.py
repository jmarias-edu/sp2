from django.shortcuts import render
from google.oauth2 import id_token
from google.auth.transport import requests
from django.conf import settings
from django.http import JsonResponse
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import authentication_classes, permission_classes
from .models import gauthuser
from rest_framework.authtoken.models import Token


import logging
logger = logging.getLogger(__name__)


# Create your views here.

@authentication_classes([])
@permission_classes([])
@csrf_exempt
@ensure_csrf_cookie
def verify_google_token(request):
    try:
        token = request.POST.get("id_token")
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), settings.GOOGLE_CLIENT_ID, clock_skew_in_seconds=3)
        userid = idinfo['sub']
        # logger.info(idinfo)

        user_fetch = gauthuser.objects.filter(user_id=userid)
        logger.info(user_fetch)

        if len(user_fetch)>0:
            user = user_fetch[0]
            logger.info("Old User!")
        else:
            user = gauthuser.objects.create(
                f_name=idinfo["given_name"], 
                l_name=idinfo["family_name"],
                email=idinfo["email"],
                user_id=userid)
            logger.info("New User!")

        fname = user.f_name
        lname = user.l_name
        email = user.email
        token, created = Token.objects.get_or_create(user=user)
    
        return JsonResponse({"success": True, "user_id": userid, "f_name": fname, "l_name": lname, "email": email, "token": token.key})

    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})

def get_user_data(request):
    return JsonResponse({"success": True})