from django.shortcuts import render
from chartit import DataPool, Chart
from .models import MyModel

data = DataPool(
    series=[{
        'options': {'source': MyModel.objects.all()},
        'terms':['x_field','y_field']
    }])
chart = Chart(
    datasource=data,
    series_options=[{'options':{'type': 'line'},'terms':{'x_field': ['y_field']}
    }],
    chart_options={'title':{'text': 'chartsPl'}})

def index(request):
    return render(request,"test1/index.html",chart)
