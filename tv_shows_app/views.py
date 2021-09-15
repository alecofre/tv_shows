from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Show

# Create your views here.
def home(request):
     # return HttpResponse('llegué a la página de inicio')
     return redirect('/shows')

def shows(request):
     all_shows = Show.objects.all()
     context = {
          'all_shows' : all_shows
     }
     return render(request,'tv_shows_app/all_shows.html', context)
     return HttpResponse('me redirigí a la página de shows')

def new_form(request):
     return render(request,'tv_shows_app/new_show_form.html')

     return HttpResponse('llegué a la página del formulario para un nuevo show')

def new_show(request):
     if request.method == "GET":
          return redirect('/shows')
     elif request.method == "POST":
          new_title = request.POST['title']
          new_network = request.POST['network']
          new_desc =  request.POST['description']
          new_date =  request.POST['release_date']

          new_show = Show.objects.create(title = new_title, network = new_network, description = new_desc, release_date = new_date)
          new_show.save()
          return redirect(f'/shows/{new_show.id}')
     
     return redirect('/shows')


def info_show(request, show_id):
     context = {
          'show' : Show.objects.get(id = show_id)
     }
     return render(request, 'tv_shows_app/info_show.html', context)
     return HttpResponse('llegué a la funcion para ver el show')

def edit_form(request, show_id):
     context = {
          'show' : Show.objects.get(id = show_id),
          'show_date' : Show.objects.get(id = show_id).release_date,          
     }
     return render(request,'tv_shows_app/edit_show_form.html', context)

     return HttpResponse('llegué a la página del formulario para un nuevo show')

def edit_show(request, show_id):
     if request.method == "GET":
          return redirect('/shows')
     elif request.method == "POST":
          new_title = request.POST['title']
          new_network = request.POST['network']
          new_desc =  request.POST['description']
          new_date =  request.POST['release_date']
          # show_id = request.POST['show_id']

          show = Show.objects.get(id = show_id)
          show.title = new_title
          show.network = new_network
          show.description = new_desc
          show.release_date = new_date
          show.save()
          return redirect(f'/shows/{show.id}')
     
     return redirect('/shows')

def delete_show(request, show_id):
     show = Show.objects.get(id = show_id)
     show.delete()
     return redirect('/shows')
     # return HttpResponse('llegué a la función para borrar un show')




