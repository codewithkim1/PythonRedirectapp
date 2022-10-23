from django.http import HttpResponseRedirect

def redirect_view(request):
    return HttpResponseRedirect('https://www.codewithkim.com/edit')