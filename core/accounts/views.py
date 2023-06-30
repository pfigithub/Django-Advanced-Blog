# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.cache import cache_page
# from django.core.cache import cache
# from .tasks import sendEmail
# import time
# import requests


# def send_email(request):
#     sendEmail.delay()
#     return HttpResponse("<h1>Done Sending</h1>")


# @cache_page
# def test(request):
#     response: requests.get("url we need")
#     return JsonResponse(response.json())