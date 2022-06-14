from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from utils.constant import *
from utils.add import sort_tasks, add_tasks
# Create your views here.

#tasks = {1: 'Pay Bills', 2: 'Workout', 3: 'Pick my sister from practice'}

class NewTaskForm(forms.Form):

    task = forms.CharField(label="Enter Your Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=50)


def index(req):

    if "tasks" not in req.session:
        req.session["tasks"] = []
    context = {'name': 'Jason', 'tasks': req.session['tasks']}
    return  render(req, URL_TASKS, context)

def add(req):

    context = {'name':'Jason', 'form':NewTaskForm()}

    if req.method == 'POST':

        
        form = NewTaskForm(req.POST)
        '''req.post returns a "QueryDict" 
        print(req.post)
        form is basically a html table
        print(form)'''

        if form.is_valid():

            task = form.cleaned_data['task']
            priority = form.cleaned_data['priority']
            '''form.cleaned_data is a dictionary
            print(form.cleaned_data)'''

            req.session['tasks'] = sort_tasks(add_tasks(req.session['tasks'], task, priority))

            #FIXME:I can improve the priority feature
            #sort_tasks(add_tasks(req.session['tasks'], task, priority))                
            
            return HttpResponseRedirect(reverse('tasks:index'))

    return render(req, URL_ADD, context)