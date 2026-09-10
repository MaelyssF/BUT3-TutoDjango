from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello Django !</h1><p>Je vous souhaite la bienvenue sur cette application Django avec la page d'accueil.</p>")

def home(request, param):
    return HttpResponse("<h1>Hello " + param + " !</h1><p>Je vous souhaite la bienvenue sur cette application Django avec la page d'accueil.</p>")

def contact(request):
    return HttpResponse("<h1>Contactez-nous !</h1><p><a href='mailto:lorem@ipsum.dolor'>Envoyer un email</a></p>")

def about(request):
    return HttpResponse("<h1>À propos de nous</h1><p>Maelyss FRONTON, étudiante de BUT3 Informatique à l'<a href='https://www.univ-orleans.fr/fr/iut-orleans'>IUT d'Orléans</a></p>")

