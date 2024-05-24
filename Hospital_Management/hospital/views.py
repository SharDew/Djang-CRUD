from django.shortcuts import render , redirect
from .models import Doctors,Patient,Ward,Patient_History
from django.views.generic import ListView,DetailView
# Create your views here.
def index(requests):
    doc = Doctors.objects.all()
    pat = Patient.objects.all()
    ward = Ward.objects.all()

    layout={
        'doctor' :doc,
        'patients' : pat,
        'wards' : ward
    }
    return render(requests, 'index.html',layout)

def doctor(requests):
    if requests.method =="GET":
        return render(requests,'doctor.html')
    else:
        doctor_id = requests.POST['idInput']
        doctor_name = requests.POST['nameInput']
        doctor_speciality = requests.POST['specialInput']
        doctor_fees = requests.POST['feesInput']
        
        Doctors.objects.create(id=doctor_id,name=doctor_name,speciality=doctor_speciality,fees=doctor_fees)
        return redirect('/')
    
def patient(requests):
    if requests.method =="GET":
        return render(requests,'patient.html')
    else:
        patient_id = requests.POST['idInput']
        patient_name = requests.POST['nameInput']
        patient_mobile = requests.POST['mobileInput']
        patient_address = requests.POST['addressInput']
        patient_issue = requests.POST['issueInput']
        if requests.POST.get('emercyInput') == "on":
            patient_emergency = True
        else:
            patient_emergency = False

        
        Patient.objects.create(id=patient_id,pname=patient_name,mobile=patient_mobile,address=patient_address,issue=patient_issue,emergency_visit=patient_emergency)

        return redirect('/')
    

def ward(requests):
    if requests.method =="GET":
        return render(requests,'ward.html')
    else:
        ward_id = requests.POST['idInput']
        ward_number = requests.POST['numberInput']
        ward_name = requests.POST['nameInput']
        ward_capacity=requests.POST['capacityInput']
        Ward.objects.create(id=ward_id,ward=ward_number,name=ward_name,capacity=ward_capacity)

        return redirect('/')
    

def delete_doc(requests,did):
    record_to_delete = Doctors.objects.get(id=did)
    record_to_delete.delete()
    return redirect('/') 


def delete_pat(requests,did):
    record_to_delete = Patient.objects.get(id=did)
    record_to_delete.delete()
    return redirect('/') 

def delete_ward(requests,did):
    record_to_delete = Ward.objects.get(id=did)
    record_to_delete.delete()
    


def edit_doctor(requests,did):
    record_to_edit = Doctors.objects.get(id=did)
    if requests.method == "GET":
        context = {'data':record_to_edit}
        return render(requests,'update_doc.html',context)
    else:
        doctor_id = requests.POST['idInput']
        doctor_name = requests.POST['nameInput']
        doctor_speciality = requests.POST['specialInput']
        doctor_fees = requests.POST['feesInput']
        record_to_edit = Doctors.objects.filter(id=did)
        record_to_edit.update(id=doctor_id,name=doctor_name,speciality=doctor_speciality,fees = doctor_fees)
        return redirect('/')
    

def edit_patient(requests,did):
    record_to_edit = Patient.objects.get(id=did)
    if requests.method == "GET":
        context = {'data':record_to_edit}
        return render(requests,'update_pat.html',context)
    else:
        patient_id = requests.POST['idInput']
        patient_name = requests.POST['nameInput']
        patient_mobile = requests.POST['mobileInput']
        patient_address = requests.POST['addressInput']
        patient_issue = requests.POST['issueInput']
        if requests.POST.get('emercyInput') == "on":
            patient_emergency = True
        else:
            patient_emergency = False
        record_to_edit = Patient.objects.filter(id=did)
        record_to_edit.update(id=patient_id,pname=patient_name,mobile=patient_mobile,address=patient_address,issue=patient_issue,emergency_visit=patient_emergency)
        return redirect('/')
    

def edit_ward(requests,did):
    record_to_edit = Ward.objects.get(id=did)
    if requests.method == "GET":
        context = {'data':record_to_edit}
        return render(requests,'update_ward.html',context)
    else:
        ward_id = requests.POST['idInput']
        ward_number = requests.POST['numberInput']
        ward_name = requests.POST['nameInput']
        ward_capacity=requests.POST['capacityInput']
        record_to_edit = Ward.objects.filter(id=did)
        record_to_edit.update(id=ward_id,ward=ward_number,name=ward_name,capacity=ward_capacity)
        return redirect('/')
    

def fil_emergency(requests):
    filter_emergency = Patient.objects.filter(emergency_visit=True)
    return render(requests,'index.html',{'emergency':filter_emergency })

def fil_issue(requests):
    data = Patient.objects.filter(issue__iexact="High Fever")
    return render(requests,'index.html',{"patients":data })

def phf(requests):
    if requests.method == "GET":
        doctor = Doctors.objects.all()
        patient = Patient.objects.all()
        context = {
            'doctors' :doctor,
            'patients' : patient
        }
        return render(requests,'patient_history_form.html',context)
    else:
        pname_id = requests.POST.get('pname')
        pname = Patient.objects.get(pk=pname_id)
        doctor_id =  requests.POST.get('doctor')
        doctor_name = Doctors.objects.get(pk=doctor_id)
        hname= requests.POST['hname']
        image = requests.FILES['pimage']
        file = requests.FILES['file']

    Patient_History.objects.create(pname=pname,hname=hname,doctor=doctor_name,pimage=image,file=file)
    return redirect('/list')

class PatientHistoryView(ListView):
    model = Patient_History
    template_name = 'display.html'

class PatientHistoryDetalView(DetailView):
    model = Patient_History
    template_name = 'detail.html'