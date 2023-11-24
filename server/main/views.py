from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadForm
from .excel_reader import parse_xls
import json


def index(request):
    return render(request, 'main/index.html')


#def update_schedule(request):
    #return render(request, 'main/update_schedule.html')


def update_schedule(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            schedule = parse_xls(form.cleaned_data['file'], 0)

            with open("shedule.json", "w") as file:  # открываем файл для записи
                json.dump(schedule, file, indent=2)

            return render(request, 'main/success.html')
    else:
        form = UploadForm()

    return render(request, 'main/update_schedule.html', {'form': form})
