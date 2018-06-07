from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

@login_required
#####################################################################
def Home(request):
    '''
        If user is authenticated, he can access the page. It 
    '''
    themes = Theme.objects.filter(
            authorized_user = request.user).order_by(
            'name')
    context = {
        'page_title': 'Animation trait de cote',
    }
    template = loader.get_template('tdc_anim/home.html')
    return HttpResponse(template.render(context, request))