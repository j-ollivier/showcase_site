from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *
from django.utils import timezone

#####################################################################
def LandingPage(request):
    '''
        Provides the main landing page information.
    '''
    context = {
        'page_title': 'Julien Ollivier',
        # 'main_page_news': main_page_news,
    }
    template = loader.get_template('main/landingpage.html')
    return HttpResponse(template.render(context, request))