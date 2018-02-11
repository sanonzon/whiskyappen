from django.db import models
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Whisky
from .forms import SearchWhiskyForm, CreateWhiskyForm

# Search for whisky
def Search(request, query=''):
    if request.method == 'POST':
        form = SearchWhiskyForm(request.POST)
        
        # Validate that shit.
        if form.is_valid():
            query_in_form = form.cleaned_data['query']

        
            result = Whisky.objects.filter(name__icontains=query_in_form)
            print(result)
            # WHen json is implemented change to return HttpResponse(result)
            return render (request, 'SearchWhisky.html', {    
                'form': SearchWhiskyForm(),
                'result': result     
            }) 
    
    else:        
        return render (request, 'SearchWhisky.html', {    
            'form': SearchWhiskyForm(),  
        })    


# Add a new whisky
def CreateWhisky(request):
    if(request.method == 'POST'):
        form = CreateWhiskyForm(request.POST)
        print(form)
        return HttpResponse('input stuff')
    else:
        return render(request, 'CreateWhisky.html',   {
            'createWhiskyForm': CreateWhiskyForm(),
            })
