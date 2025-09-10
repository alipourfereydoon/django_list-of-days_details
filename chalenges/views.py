from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.template.loader import render_to_string

days = {
    'sunday':'today is sunday',
    'monday':'today is monday',
    'tuseday':'today is tuesday',
    'thursday':'today is thuresday',
    'friday':'today is friday',
    'saturday':'today is saturday',
}

def dynamic_days_numbr(request,day):
    days_date = list(days.keys())
    if day > len(days_date):
        return HttpResponseNotFound("this page not found")
    redirect_day =days_date[day-1]
    return HttpResponseRedirect(redirect_day)

def dynamic_days(request,day):
    days_date = days.get(day)
    if days_date is not None:  
        return render(request , 'chalenges/chalenge.html',context={'day_data':days_date})
        # response_data = render_to_string('chalenges/chalenge.html') 
        # return HttpResponse(response_data)
    return HttpResponseNotFound('this page is not exist')

def list_days(request):
    days_list = list(days.keys())
    list_item = ""
    for item in days_list:
        list_item += f'<li><a href="{item}">{item}</a></li>'
        
    content = f'<ul>{list_item}</ul>'
    return HttpResponse(content)

