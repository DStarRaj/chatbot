from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .chat.context import Chatter

A = Chatter()
CHAT = []


# Create your views here.
def members(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(
        template.render(context, request)
    )

def send(request):
    message = request.POST['message']
    print(message)
    CHAT.append(
        (
        "user",
        message
        )
    )

    CHAT.append(
        (
        "bot",
        A.resp(message)
        )
    )
    print(f"send-----: {CHAT}")
    return HttpResponse(f'{CHAT} sent successfully')

def getMessages(request):
    print(CHAT)
    return JsonResponse({"messages":CHAT})