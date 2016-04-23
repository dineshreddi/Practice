from django.shortcuts import render
from djangoapp.models import person
from django.db.models import Q
from django.template import RequestContext

# Create your views here.
from django.http import HttpResponse
def djangopage(request):
    return HttpResponse("welcome to application")
def load_login(request):
    return render(request,'loginpage.html')
def load_register(request):
    return render(request,'register.html')
def show_details(request):
    names=person.objects.filter(Q(age__gt=22))
    return render_to_response("person_details.html",{'details':name})

def do_registration(request):
    import pdb
    pdb.set_trace()
    data = request.POST
    try:
        obj = person(name=data.get('name'),
                     age=int(data.get('age')),
                     email=data.get('email'),
                     phone=int(data.get('phone')),
                     gender=data.get('gender'),
                     location=data.get('loc'),
                     marital_status=data.get('ms'))
        obj.save()
    except Exception as e:
        print str(e)
        pass
    finally:
        pass
    return HttpResponse('User registered successfully', RequestContext(request))
                 
