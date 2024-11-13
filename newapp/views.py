from django.shortcuts import render
# Create your views here.
def num(request):
    data1 = {'numbers': [ 12, 45, 56, 48]}
    return render(request, 'numbers.html', data1)



def img(request):
    return render(request,'image.html')