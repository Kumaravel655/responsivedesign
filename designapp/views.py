from django.shortcuts import render

# Create your views here.
def responsiveproducts(request):
    context = {}
    return render(request,'designapp/responsiveproducts.html',context)

def responsivepage(request):
    context = {}
    return render(request,'designapp/responsivepage.html',context) 