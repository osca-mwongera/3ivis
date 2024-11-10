from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required
def index(request):
    """ "
    This function view is based on Django. It renders a template of the chart
    It requires one to be logged in.
    """
    return render(request=request, template_name="chart/chart.html", context={})
