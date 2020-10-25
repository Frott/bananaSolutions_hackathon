from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import models
from django.urls import reverse
from bananaApp.auth_helper import get_sign_in_url, get_token_from_code, store_token, store_user, remove_user_and_token, get_token
from bananaApp.graph_helper import get_user
from django.views.generic import TemplateView
# Create your views here.
def offer_view(request):
    offer_list = models.offer.objects.order_by('offer_id')
    offer_dict = {'offers':offer_list}
    return render(request, 'bananaApp/index.html', context=offer_dict)

def dyn_view(request, my_id):
    obj = models.offer.objects.get(id=my_id)
    context = {
        "object": obj
    }
    return render(request, 'bananaApp/offer.html', context)

def sign_in(request):
  # Get the sign-in URL
  sign_in_url, state = get_sign_in_url()
  # Save the expected state so we can validate in the callback
  request.session['auth_state'] = state
  request.session.modified = True
  # Redirect to the Azure sign-in page
  return HttpResponseRedirect(sign_in_url)

def sign_out(request):
  # Clear out the user and token
  remove_user_and_token(request)

  return HttpResponseRedirect(reverse('index'))

def callback(request):
  # Get the state saved in session
  expected_state = request.session.pop('auth_state', '')
  # Make the token request
  token = get_token_from_code(request.get_full_path(), expected_state)

  # Get the user's profile
  user = get_user(token)
  # Temporary! Save the response in an error so it's displayed
  request.session['flash_error'] = { 'message': 'Token retrieved',
    'debug': 'User: {0}\nToken: {1}'.format(user, token) }
  return HttpResponseRedirect(reverse('index'))