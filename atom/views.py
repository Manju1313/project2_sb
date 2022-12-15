from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import people,marks
from .forms import *
from django.contrib import messages
from .models import *
from.forms import *

# Create your views here.
def index(request):
  mymem = people.objects.all().values()
  context = {
    'mymembers': mymem,
  }
  
  return render(request,'index.html',context)


def sun(request):
    mymarks =marks.objects.all()
    context = {
        'mymarks':mymarks,
    }
    return render(request,'marks.html',context)


def check(request):
    return render(request,'response.html')


def root(request):
        
    return render(request,"Define.html")



def sample(request):
  return render(request,'Sample.html')

def main(request):
    return render(request,'registerform.html')

def scan(request):
    return render(request,'post.html')


def method(request):
    form = NameForm
    mydict ={
        'form':form
    }

    return render(request, 'form.html',context=mydict)

    	# if request.method == "POST":
	# 	move_form = peopleForm(request.POST, request.FILES)
	# 	if move_form.is_valid():
	# 		move_form.save()
	# 		messages.success(request, ('Your move was successfully added!'))
	# 	else:
	# 		messages.error(request, 'Error saving form')
		
		
	# 	return redirect("index.html")
	# move_form = peopleForm()
	# move = people.objects.all()
	# return render(request=request, template_name="form.html", context={'move_form':move_form, 'move':move})


def forms(request):
    NF=NameForm()
    d={'form':NF}
    if request.method=='POST':
        form_data=NameForm(request.POST)
        if form_data.is_valid():
            #return HttpResponse(str(form_data.cleaned_data))
            n=form_data.cleaned_data['name']
            a=form_data.cleaned_data['age']
            g=form_data.cleaned_data['gender']
            
            c=form_data.cleaned_data['course']
            d1={'n':n,'a':a,'g':g,'c':c}
            return render(request,'data.html',d1)
    return render(request,'djangoforms.html',d)

def insert(request):
    TF=TopicForm()
    d={'form':TF}
    if request.method=='POST':
        form_data=TopicForm(request.POST)
        if form_data.is_valid():
            tn=form_data.cleaned_data['topic']
            dt=form_data.cleaned_data['date']
            # T=Topic.objects.get_or_create(topic_name=tn,date=dt)[0]
            # T.save()
            return HttpResponse('Inserted')
    return render(request,'insert_form.html',d)

