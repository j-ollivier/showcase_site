from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *
from .forms import *
from django.utils import timezone
from django.contrib import messages

#####################################################################
def LandingPage(request):
    '''
        Provides the main landing page information.
    '''
    context = {
        'page_title': 'Julien Ollivier',
    }
    template = loader.get_template('main/landingpage.html')
    return HttpResponse(template.render(context, request))

#####################################################################
def Prestations(request):
    '''
        Provides the prestation informations
    '''
    context = {
        'page_title': 'Prestations',
    }
    template = loader.get_template('main/prestations.html')
    return HttpResponse(template.render(context, request))

#####################################################################
def Portfolio(request):
    '''
        Provides the main landing page information.
    '''
    context = {
        'page_title': 'Portfolio',
    }
    template = loader.get_template('main/portfolio.html')
    return HttpResponse(template.render(context, request))

#####################################################################
def Contact(request):
    '''
        Simple contact view
    '''
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            new_message = ContactMessage()
            new_message.nom = form.cleaned_data['nom']
            new_message.contenu = form.cleaned_data['contenu']
            new_message.remote_addr = request.META['REMOTE_ADDR']
            new_message.timestamp = timezone.now()
            # # basic spam/double POST checker
            # existing_message = ContactMessage.objects.filter()
            new_message.save()
            messages.success(request, 'Votre message a bien été envoyé, \
                vous recevrez une réponse rapidement.')
        else:
            messages.error(request, 'Une erreur est survenue. \
                Veuillez nous contacter par un autre moyen.')
    else:
        pass
    context = {
        'page_title': 'Contact',
        'contact_form' : ContactMessageForm(),
        # 'main_page_news': main_page_news,
    }
    template = loader.get_template('main/contact.html')
    return HttpResponse(template.render(context, request))

#####################################################################
def License(request):
    '''
        Provides the licence information
    '''
    context = {
        'page_title': 'License',
    }
    template = loader.get_template('main/license.html')
    return HttpResponse(template.render(context, request))