from django.contrib import admin

# Register your models here.
from .models import LanguageImg
admin.site.register(LanguageImg)

from .models import CurrentLangImg
admin.site.register(CurrentLangImg)

from .models import EducationsQuali
admin.site.register(EducationsQuali)

from .models import Projects
admin.site.register(Projects)