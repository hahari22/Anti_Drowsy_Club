from django.shortcuts import render
from django.http import HttpResponse
import drow.tts as tts

# Create your views here. 
def home(request): # 의미 없는 path 입니다. 신경 쓰지 마세요.
    return HttpResponse('Hello')

def setting(request): # 알람을 만드는 부분 입니다.
    if request.method == 'GET' :
        return render(request, 'chat/setting.html',{})
    elif request.method == 'POST':
        content = request.POST['sound-content-input']
        name = tts.make_tts(content,'alarm')
        return HttpResponse(name)
    
def room(request, room_name):
    return render(request, 'chat/room.html',{
        'room_name':room_name
    })
