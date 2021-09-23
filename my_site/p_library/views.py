from django.shortcuts import render
from p_library.models import *
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

# Create your views here.

def index(request):
	template = loader.get_template('index.html')
	books = Book.objects.all()
	biblio_data = {
		"books":books
	}
	return HttpResponse(template.render(biblio_data, request))

def publishers(request):
    template = loader.get_template('publishers.html')
    publishers = Publisher.objects.all()
    publishers_data = {
        "publishers":publishers
    }
    return HttpResponse(template.render(publishers_data, request))