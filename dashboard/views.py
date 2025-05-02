from django.shortcuts import render
from django.http import HttpResponse
from .models import LanguageImg
from .models import CurrentLangImg
from .models import EducationsQuali
from .models import Projects


# Create your views here.
def index(request):
    language_img = LanguageImg.objects.all()
    current_lang_img = CurrentLangImg.objects.all()
    educations_quali = EducationsQuali.objects.all()
    project = Projects.objects.all()
    params = {
        'language_img': language_img, 
        'current_lang_img': current_lang_img,
        'educations_quali': educations_quali,
        'project': project,

         }

    return render(request, 'index.html',params)
