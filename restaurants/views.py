from django.shortcuts import render


# Create your views here.
def you_f_view(request):
   conext={'msg': "Hello World!"}
   return render(request,'re.html',conext)
