from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from Specialty.models import doctor
#پوست

def List(request):
    doctor_list = doctor.objects.all()
    derma_doctor_list = []
    for doci in doctor_list:
        if doci.Specialty.Name == 'Dermatology':
            derma_doctor_list.append({
                'Name' : doci.Name,
                'Speciality' : doci.Specialty.Name
            })
    return JsonResponse(derma_doctor_list, safe=False)

def List_html(request):
    doctors = doctor.objects.all()
    doctors_list = []
    for item in doctors:
        print(item.Specialty.Name)
        if item.Specialty.Name == 'Dermatology':
            print('Found')
            doctors_list.append(item)
    doctors_json = {'Doctor' : doctors_list}
    return render(request, 'Logy/logy.html', doctors_json)