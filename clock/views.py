from django.shortcuts import render
import datetime as dt
# Create your views here.
now = dt.datetime.now()
def clock(request):
    return render(request,"time.html",{
        "h":now.hour,
        "m":now.minute,
        "s":now.second,

    })