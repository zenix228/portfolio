from django.shortcuts import render, get_object_or_404
from .models import Portfolio
from apps.about.models import About

def product_list(request):
    portfolio = None
    portfolioo = Portfolio.objects.all()

    context = {
        'portfolio': portfolio,
        'portfolioo': portfolioo
    }
    template_name = 'portfolio/index.html'

    return render(
        request,
        template_name,
        context
    )
