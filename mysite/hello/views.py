
from django.http import HttpResponse
# Create your views here.

def myview(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    resp = HttpResponse('view count='+str(num_visits)+'string is:  ea6abe1f ')
    resp.set_cookie('dj4e_cookie', 'ea6abe1f', max_age=1000)
    return resp
