from django.shortcuts import render
from .models import Area, Title, Service


def smart_home_view(request):

    '''if request.method == 'POST' :
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
    else :
        form = ContactForm()'''
 
    areas = Area.objects.all()
    titles = Title.objects.all()

    context = {'areas':areas, 'titles':titles}

    return render(request, 'Smart/smart_home.html', context)


"""def smart_contact_view(request):
    areas = Area.objects.all()
    titles = Title.objects.all() 
    context = {'areas':areas, 'titles':titles}
    return render(request, 'Smart/smart_contact.html', context)

def smart_service_view(request):

    titles = Title.objects.all()
    services =  Service.objects.all()
    context = {'services' : services, 'titles':titles}  
    return render(request, 'Smart/smart_service.html', context)



def smart_area_view(request):

    titles = Title.objects.all()
    services = Service.objects.all()
    context = {'services':services, 'titles':titles}
    return render(request, 'Smart/smart_area.html', context)


def smart_team_view(request):
    areas = Area.objects.all()
    titles = Title.objects.all()
    context = {'areas':areas, 'titles':titles}
    return render(request, 'Smart/smart_team.html', context)


def smart_who_are_we_view(request):

    titles = Title.objects.all()
    context = {'titles':titles}

    return render(request, 'Smart/smart_who_are_we.html', context)"""

