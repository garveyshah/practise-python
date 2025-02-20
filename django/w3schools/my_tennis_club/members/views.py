from django.template import loader
from django.http import HttpResponse
from .models import Member

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def myworld(request):
    return HttpResponse("This is my World !")



# def members(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())

