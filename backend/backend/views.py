from django.shortcuts import render,HttpResponse
from django.views.generic import View

class indexView(View):
    def get(self,request):
        return render(request,"index.html")
    
class logout(View):
    def get(self,request):
        response = render(request,"index.html")
        response.delete_cookie('token')
        return response