from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
import pytz


# Create your views here.
def stage0_view(request):
    response_data = {
        "email": "shoyebo98@gmail.com",
        "current_datetime": datetime.now(pytz.UTC).isoformat(),
        "github_url": "https://github.com/ShoyeboMoses/HNG.git"
    }
    return JsonResponse(response_data)