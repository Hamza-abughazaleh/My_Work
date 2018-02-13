from django.views.genaric import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'
