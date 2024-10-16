from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def omlet(request):
    dash ={}

    recepts = DATA['omlet']
    quant = float(request.GET.get('servings', 1))
    if quant == 'NoneType':
        dash == recept
    
    else:
        for k, v in recepts.items():
            quantity = float(v)*quant
            dash[k] = quantity


    context = { 
             'recept': dash,
    
    }

    return render(request, 'recip.html', context) 


def pasta(request):
    dash ={}

    recepts = DATA['pasta']
    quant = float(request.GET.get('servings', 1))
    if quant == 'NoneType':
        dash == recept
    
    else:
        for k, v in recepts.items():
            quantity = float(v)*quant
            dash[k] = quantity


    context = { 
             'recept': dash,
    
    }

    return render(request, 'recip.html', context)  


def buter(request):
    dash ={}

    recepts = DATA['buter']
    quant = float(request.GET.get('servings', 1))
    if quant == 'NoneType':
        dash == recept
    
    else:
        for k, v in recepts.items():
            quantity = float(v)*quant
            dash[k] = quantity


    context = { 
             'recept': dash,
    
    }

    return render(request, 'recip.html', context)               