from django.shortcuts import render

def  hello():
    resp = HttpResponse('a797b6a1')
    resp.set_cookie('dj4e_cookie', 'a797b6a1', max_age=1000)
    return resp
