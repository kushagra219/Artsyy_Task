from django.shortcuts import render, redirect
from .models import * 
from .forms import * 
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
# Create your views here.


class AppointmentsForAPatientView(ListView):

    def get_queryset(self):
        return Appointment.objects.filter(patient=self.request.user)


class AppointmentsForADoctorView(ListView):

    def get_queryset(self):
        return Appointment.objects.filter(doctor=self.request.user)


class MedicalHistoryView(ListView):

    def get_queryset(self):
        return Prescription.objects.filter(patient=self.request.user)


class PrescriptionListView(ListView):

    def get_queryset(self):
        return Prescription.objects.filter(doctor=self.request.user)

def PrescriptionCreateView(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.doctor = request.user
            prescription.save()
            return redirect('appointment:doc-prescriptions')
    else:
        form = PrescriptionForm()
    return render(request, 'appointment/prescription_create.html', {'form': form})

    