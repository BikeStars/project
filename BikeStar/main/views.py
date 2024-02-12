from django.shortcuts import render, redirect
from .models import Route
from .forms import RouteForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy

from django.contrib.auth import get_user_model


User = get_user_model()


def index(request):
    title = request.GET.get('query')
    if title:
        routes = Route.objects.filter(title__icontains=title)
    else:
        routes = Route.objects.all()
    context = {'routes': routes,
               'title': title,
               }
    return render(request, 'main/index.html', context)


@login_required(login_url=reverse_lazy('login'))
def main_post(request):
    if request.method == 'POST':
        form = RouteForm(request.POST, request.FILES)
        if form.is_valid():
            route = Route(**form.cleaned_data)
            route.user = request.user
            route.save()
            url = reverse('main_page')
            return redirect(url)
    else:
        form = RouteForm()
    context = {'form': form}
    return render(request, 'main/main-post.html', context)


def main_detail(request, pk):
    route = Route.objects.get(id=pk)
    context = {
        'route': route
    }
    return render(request, 'main/main.html', context)