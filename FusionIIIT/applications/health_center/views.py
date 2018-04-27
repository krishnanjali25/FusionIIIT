import json
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from applications.globals.models import ExtraInfo

<<<<<<< HEAD
from .models import (Ambulance_request, Appointment, Complaint, Constants, Counter, Expiry,
                     Doctor, Hospital_admit, Medicine, Prescribed_medicine, Hospital,
                     Prescription, Schedule, Stock)
=======
from .models import (Ambulance_request, Appointment, Complaint, Constants,
                     Doctor, Hospital_admit, Medicine, Prescribed_medicine,
                     Prescription, Schedule, Stock, Stockinventory)
>>>>>>> da2946e1cfafc8a828075685182d40ebba922cd8


def datetime_handler(x):
    if hasattr(x, 'isoformat'):
        return x.isoformat()
    else:
        raise TypeError

<<<<<<< HEAD
@login_required
def healthcenter(request):
    usertype = ExtraInfo.objects.get(user=request.user).user_type

    if usertype == 'student' or usertype=='faculty' or usertype=='staff':
=======

@login_required
def healthcenter(request):
    usertype = ExtraInfo.objects.get(user=request.user).user_type
    if usertype == 'student':
>>>>>>> da2946e1cfafc8a828075685182d40ebba922cd8
        return HttpResponseRedirect("/healthcenter/student")
    elif usertype == 'compounder':
        return HttpResponseRedirect("/healthcenter/compounder")


@login_required
def compounder_view(request):
<<<<<<< HEAD
=======

>>>>>>> da2946e1cfafc8a828075685182d40ebba922cd8
    usertype = ExtraInfo.objects.get(user=request.user).user_type
    if usertype == 'compounder':
        if request.method == 'POST':

            if 'feed_com' in request.POST:
<<<<<<< HEAD
=======
                print("anjali")
>>>>>>> da2946e1cfafc8a828075685182d40ebba922cd8
                pk = request.POST.get('com_id')
                feedback = request.POST.get('feed')
                Complaint.objects.filter(id=pk).update(feedback=feedback)
                data = {'feedback': feedback}
                return JsonResponse(data)
            elif 'end' in request.POST:
                pk = request.POST.get('id')
<<<<<<< HEAD
                Ambulance_request.objects.filter(id=pk).update(end_date=datetime.now())
                amb=Ambulance_request.objects.filter(id=pk)
                for f in amb:
                    dateo=f.end_date
                data={'datenow':dateo}
                return JsonResponse(data)
            elif 'returned' in request.POST:
                pk = request.POST.get('id')
                Expiry.objects.filter(id=pk).update(returned=True,return_date=datetime.now())
                qty=Expiry.objects.get(id=pk).quantity
                med=Expiry.objects.get(id=pk).medicine_id.id
                quantity=Stock.objects.get(id=med).quantity
                quantity=quantity-qty
                Stock.objects.filter(id=med).update(quantity=quantity)
                data={'status':1}
                return JsonResponse(data)
            elif 'add_doctor' in request.POST:
                doctor=request.POST.get('new_doctor')
                specialization=request.POST.get('specialization')
                phone=request.POST.get('phone')
                Doctor.objects.create(
                doctor_name=doctor,
                doctor_phone=phone,
                specialization=specialization,
                active=True
                )
                data={'status':1}
                return JsonResponse(data)
            elif 'remove_doctor' in request.POST:
                doctor=request.POST.get('doctor_active')
                Doctor.objects.filter(id=doctor).update(active=False)
                data={'status':1}
                return JsonResponse(data)
            elif 'discharge' in request.POST:
                pk = request.POST.get('id')
                Hospital_admit.objects.filter(id=pk).update(discharge_date=datetime.now())
                hosp=Hospital_admit.objects.filter(id=pk)
                for f in hosp:
                    dateo=f.discharge_date
                data={'datenow':dateo}
=======
                Ambulance_request.objects.filter(
                    id=pk).update(end_date=datetime.now())
                amb = Ambulance_request.objects.filter(id=pk)
                for f in amb:
                    dateo = f.end_date
                data = {'datenow': dateo}
                return JsonResponse(data)
            elif 'discharge' in request.POST:
                pk = request.POST.get('id')
                Hospital_admit.objects.filter(id=pk).update(
                    discharge_date=datetime.now())
                hosp = Hospital_admit.objects.filter(id=pk)
                for f in hosp:
                    dateo = f.discharge_date
                data = {'datenow': dateo}
>>>>>>> da2946e1cfafc8a828075685182d40ebba922cd8
                return JsonResponse(data)
            elif 'add_stock' in request.POST:
                medicine = request.POST.get('medicine_id')
                medicine_name = Stock.objects.get(id=medicine)
                qty = int(request.POST.get('quantity'))
<<<<<<< HEAD
                supplier=request.POST.get('supplier')
                expiry=request.POST.get('expiry_date')
                Expiry.objects.create(
                    medicine_id=medicine_name,
                    quantity=qty,
                    supplier=supplier,
                    expiry_date=expiry,
                    date=datetime.now(),
=======
                Stockinventory.objects.create(
                    medicine_id=medicine_name,
                    quantity=qty,
                    date=datetime.now()
>>>>>>> da2946e1cfafc8a828075685182d40ebba922cd8
                )
                quantity = (Stock.objects.get(id=medicine)).quantity
                quantity = quantity + qty
                Stock.objects.filter(id=medicine).update(quantity=quantity)
<<<<<<< HEAD
                data={'status':1}
=======
                data = {'status': 1}
>>>>>>> da2946e1cfafc8a828075685182d40ebba922cd8
                return JsonResponse(data)
            elif 'edit' in request.POST:
                doctor = request.POST.get('doctor')
                day = request.POST.get('day')
                time_in = request.POST.get('time_in')
                time_out = request.POST.get('time_out')
                room = request.POST.get('room')
                sc = Schedule.objects.filter(doctor_id=doctor, day=day)
                doctor_id = Doctor.objects.get(id=doctor)
                if sc.count() == 0:
                    Schedule.objects.create(doctor_id=doctor_id, day=day, room=room,
                                            from_time=time_in, to_time=time_out)
                else:
<<<<<<< HEAD
                    Schedule.objects.filter(doctor_id=doctor_id, day=day).update(room=room)
                    Schedule.objects.filter(doctor_id=doctor_id, day=day).update(from_time=time_in)
                    Schedule.objects.filter(doctor_id=doctor_id, day=day).update(to_time=time_out)
=======
                    Schedule.objects.filter(
                        doctor_id=doctor_id, day=day).update(room=room)
                    Schedule.objects.filter(
                        doctor_id=doctor_id, day=day).update(from_time=time_in)
                    Schedule.objects.filter(
                        doctor_id=doctor_id, day=day).update(to_time=time_out)
>>>>>>> da2946e1cfafc8a828075685182d40ebba922cd8
                data = {}
                return JsonResponse(data)
            elif 'add_medicine' in request.POST:
                medicine = request.POST.get('new_medicine')
                quantity = request.POST.get('new_quantity')
                threshold = request.POST.get('threshold')
<<<<<<< HEAD
                new_supplier = request.POST.get('new_supplier')
                new_expiry_date = request.POST.get('new_expiry_date')
=======
>>>>>>> da2946e1cfafc8a828075685182d40ebba922cd8
                Stock.objects.create(
                    medicine_name=medicine,
                    quantity=quantity,
                    threshold=threshold
                )
                medicine_id = Stock.objects.get(medicine_name=medicine)
<<<<<<< HEAD
                Expiry.objects.create(
                    medicine_id=medicine_id,
                    quantity=quantity,
                    supplier=new_supplier,
                    expiry_date=new_expiry_date,
                    returned=False,
                    return_date=None,
                    date=datetime.now()
                )
                data={'status':1}
                return JsonResponse(data)
            elif 'user_p' in request.POST:
                app = Appointment.objects.filter(user_id=request.POST.get('user_p'),date=datetime.now())
=======
                Stockinventory.objects.create(
                    medicine_id=medicine_id,
                    quantity=quantity,
                    date=datetime.now()
                )
                data = {'status': 1}
                return JsonResponse(data)
            elif 'user_p' in request.POST:
                app = Appointment.objects.filter(
                    user_id=request.POST.get('user_p'), date=datetime.now())
                print(app)
>>>>>>> da2946e1cfafc8a828075685182d40ebba922cd8
                if app:
                    s = 1
                else:
                    s = 0
<<<<<<< HEAD
                data={'status': s}
=======
                data = {'status': s}
>>>>>>> da2946e1cfafc8a828075685182d40ebba922cd8
                return JsonResponse(data)
            elif 'admission' in request.POST:
                user = request.POST.get('user_id')
                user_id = ExtraInfo.objects.get(id=user)
                doctor = request.POST.get('doctor_id')
                doctor_id = Doctor.objects.get(id=doctor)
                admission_date = request.POST.get('admission_date')
                reason = request.POST.get('description')
                hospital_doctor = request.POST.get('hospital_doctor')
<<<<<<< HEAD
                hospital_id = request.POST.get('hospital_name')
                hospital_name=Hospital.objects.get(id=hospital_id)
                Hospital_admit.objects.create(
                     user_id=user_id,
                     doctor_id=doctor_id,
                     hospital_name=hospital_name,
                     admission_date=admission_date,
                     hospital_doctor=hospital_doctor,
                     discharge_date=None,
                     reason=reason
                 )
                data={'status':1}
=======
                hospital_name = request.POST.get('hospital_name')
                Hospital_admit.objects.create(
                    user_id=user_id,
                    doctor_id=doctor_id,
                    hospital_name=hospital_name,
                    admission_date=admission_date,
                    hospital_doctor=hospital_doctor,
                    discharge_date=None,
                    reason=reason
                )
                data = {'status': 1}
>>>>>>> da2946e1cfafc8a828075685182d40ebba922cd8
                return JsonResponse(data)
            elif 'medicine_name' in request.POST:
                app = request.POST.get('user')
                user = Appointment.objects.get(id=app).user_id
                quantity = int(request.POST.get('quantity'))
                days = int(request.POST.get('days'))
                times = int(request.POST.get('times'))
                medicine_id = request.POST.get('medicine_name')
                medicine = Stock.objects.get(id=medicine_id)
                Medicine.objects.create(
                    patient=user,
                    medicine_id=medicine,
                    quantity=quantity,
                    days=days,
                    times=times
                )
                schs = Medicine.objects.all()
                list = []
                for s in schs:
                    list.append({'medicine': s.medicine_id.medicine_name, 'quantity': s.quantity,
                                 'days': s.days, 'times': s.times})
                sches = json.dumps(list, default=datetime_handler)
                return HttpResponse(sches, content_type='json')
            elif 'day' in request.POST:
                day = request.POST.get('day')
                sche = Schedule.objects.filter(day=day)
                list = []
                for s in sche:
                    list.append({'room': s.room, 'id': s.id, 'doctor': s.doctor_id.doctor_name,
                                 'from_time': s.from_time, 'to_time': s.to_time})

                sches = json.dumps(list, default=datetime_handler)
                return HttpResponse(sches, content_type='json')
            elif 'medicine_name_b' in request.POST:
                user_id = request.POST.get('user')
                user = ExtraInfo.objects.get(id=user_id)
                quantity = int(request.POST.get('quantity'))
                days = int(request.POST.get('days'))
                times = int(request.POST.get('times'))
                medicine_id = request.POST.get('medicine_name_b')
                medicine = Stock.objects.get(id=medicine_id)
                Medicine.objects.create(
                    patient=user,
                    medicine_id=medicine,
                    quantity=quantity,
                    days=days,
                    times=times
                )
                schs = Medicine.objects.all()
                list = []
                for s in schs:
                    list.append({'medicine': s.medicine_id.medicine_name, 'quantity': s.quantity,
                                 'days': s.days, 'times': s.times})
                sches = json.dumps(list, default=datetime_handler)
                return HttpResponse(sches, content_type='json')
            elif 'day' in request.POST:
                day = request.POST.get('day')
                sche = Schedule.objects.filter(day=day)
                list = []
                for s in sche:
                    list.append({'room': s.room, 'id': s.id, 'doctor': s.doctor_id.doctor_name,
                                 'from_time': s.from_time, 'to_time': s.to_time})

                sches = json.dumps(list, default=datetime_handler)
                return HttpResponse(sches, content_type='json')
            elif 'main' in request.POST:
                data = {
<<<<<<< HEAD
                        'status': 1
                        }
=======
                    'status': 1
                }
>>>>>>> da2946e1cfafc8a828075685182d40ebba922cd8
                return JsonResponse(data)
            elif 'doct' in request.POST:
                doctor_id = request.POST.get('doct')
                schedule = Schedule.objects.filter(doctor_id=doctor_id)
                list = []
                for s in schedule:
                    list.append({'room': s.room, 'id': s.id, 'doctor': s.doctor_id.doctor_name,
                                 'day': s.get_day_display(), 'from_time': s.from_time,
                                 'to_time': s.to_time})

                sches = json.dumps(list, default=datetime_handler)
                return HttpResponse(sches, content_type='json')

            elif 'prescribe' in request.POST:
                app_id = request.POST.get('user')
                details = request.POST.get('details')
                tests = request.POST.get('tests')
                appointment = Appointment.objects.get(id=app_id)
<<<<<<< HEAD
                user=appointment.user_id
                doctor=appointment.doctor_id
=======
                user = appointment.user_id
                doctor = appointment.doctor_id
>>>>>>> da2946e1cfafc8a828075685182d40ebba922cd8
                Prescription.objects.create(
                    user_id=user,
                    doctor_id=doctor,
                    details=details,
                    date=datetime.now(),
                    test=tests,
                    appointment=appointment
                )
                query = Medicine.objects.filter(patient=user)
                prescribe = Prescription.objects.all().last()
                for medicine in query:
                    medicine_id = medicine.medicine_id
                    quantity = medicine.quantity
                    days = medicine.days
                    times = medicine.times
                    Prescribed_medicine.objects.create(
                        prescription_id=prescribe,
                        medicine_id=medicine_id,
                        quantity=quantity,
                        days=days,
                        times=times
                    )
<<<<<<< HEAD
                    today=datetime.now()
                    expiry=Expiry.objects.filter(medicine_id=medicine_id,quantity__gt=0,returned=False,expiry_date__gte=today).order_by('expiry_date')
                    stock=Stock.objects.get(medicine_name=medicine_id).quantity
                    if stock>quantity:
                        for e in expiry:
                            q=e.quantity
                            em=e.id
                            if q>quantity:
                                q=q-quantity
                                Expiry.objects.filter(id=em).update(quantity=q)
                                qty = Stock.objects.get(medicine_name=medicine_id).quantity
                                qty = qty-quantity
                                Stock.objects.filter(medicine_name=medicine_id).update(quantity=qty)
                                break
                            else:
                                quan=Expiry.objects.get(id=em).quantity
                                Expiry.objects.filter(id=em).update(quantity=0)
                                qty = Stock.objects.get(medicine_name=medicine_id).quantity
                                qty = qty-quan
                                Stock.objects.filter(medicine_name=medicine_id).update(quantity=qty)
                                quantity=quantity-quan
                        status=1
                    else:
                        status=0

                    Medicine.objects.all().delete()
                    data = {
                            'status': status,
                            'stock':stock
                            }
=======
                    qty = Stock.objects.get(medicine_name=medicine_id).quantity
                    qty = qty-quantity
                    Stock.objects.filter(
                        medicine_name=medicine_id).update(quantity=qty)
                    Medicine.objects.all().delete()
                    data = {
                        'status': 1
                    }
>>>>>>> da2946e1cfafc8a828075685182d40ebba922cd8
                return JsonResponse(data)
            elif 'prescribe_b' in request.POST:
                user_id = request.POST.get('user')
                user = ExtraInfo.objects.get(id=user_id)
                doctor_id = request.POST.get('doctor')
                if doctor_id == "":
                    doctor = None
                else:
                    doctor = Doctor.objects.get(id=doctor_id)
                details = request.POST.get('details')
                tests = request.POST.get('tests')
<<<<<<< HEAD
                app = Appointment.objects.filter(user_id=user_id,date=datetime.now())
                if app:
                    appointment = Appointment.objects.get(user_id=user_id,date=datetime.now())
=======
                app = Appointment.objects.filter(
                    user_id=user_id, date=datetime.now())
                print(app)
                if app:
                    appointment = Appointment.objects.get(
                        user_id=user_id, date=datetime.now())
>>>>>>> da2946e1cfafc8a828075685182d40ebba922cd8
                else:
                    appointment = None
                Prescription.objects.create(
                    user_id=user,
                    doctor_id=doctor,
                    details=details,
                    date=datetime.now(),
                    test=tests,
                    appointment=appointment
                )
                query = Medicine.objects.filter(patient=user)
                prescribe = Prescription.objects.all().last()
                for medicine in query:
                    medicine_id = medicine.medicine_id
                    quantity = medicine.quantity
                    days = medicine.days
                    times = medicine.times
                    Prescribed_medicine.objects.create(
                        prescription_id=prescribe,
                        medicine_id=medicine_id,
                        quantity=quantity,
                        days=days,
                        times=times
                    )
<<<<<<< HEAD
                    today=datetime.now()
                    expiry=Expiry.objects.filter(medicine_id=medicine_id,quantity__gt=0,returned=False,expiry_date__gte=today).order_by('expiry_date')
                    stock=Stock.objects.get(medicine_name=medicine_id).quantity
                    if stock>quantity:
                        for e in expiry:
                            q=e.quantity
                            em=e.id
                            if q>quantity:
                                q=q-quantity
                                Expiry.objects.filter(id=em).update(quantity=q)
                                qty = Stock.objects.get(medicine_name=medicine_id).quantity
                                qty = qty-quantity
                                Stock.objects.filter(medicine_name=medicine_id).update(quantity=qty)
                                break
                            else:
                                quan=Expiry.objects.get(id=em).quantity
                                Expiry.objects.filter(id=em).update(quantity=0)
                                qty = Stock.objects.get(medicine_name=medicine_id).quantity
                                qty = qty-quan
                                Stock.objects.filter(medicine_name=medicine_id).update(quantity=qty)
                                quantity=quantity-quan
                        status=1
                    else:
                        status=0

                    Medicine.objects.all().delete()
                    data = {
                            'status': status
                            }
=======
                    qty = Stock.objects.get(medicine_name=medicine_id).quantity
                    qty = qty-quantity
                    Stock.objects.filter(
                        medicine_name=medicine_id).update(quantity=qty)
                    Medicine.objects.all().delete()
                    data = {
                        'status': 1
                    }
>>>>>>> da2946e1cfafc8a828075685182d40ebba922cd8
                return JsonResponse(data)

        else:
            all_complaints = Complaint.objects.all()
            all_hospitals = Hospital_admit.objects.all().order_by('-admission_date')
            all_ambulances = Ambulance_request.objects.all().order_by('-date_request')
<<<<<<< HEAD
            appointments_today =Appointment.objects.filter(date=datetime.now()).order_by('date')
            appointments_future=Appointment.objects.filter(date__gt=datetime.now()).order_by('date')
            users = ExtraInfo.objects.filter(user_type='student')
            doctors = Doctor.objects.all()
            stocks = Stock.objects.all()
            days = Constants.DAYS_OF_WEEK
            schedule=Schedule.objects.all().order_by('doctor_id')
            expired=Expiry.objects.filter(expiry_date__lt=datetime.now(),returned=False).order_by('expiry_date')
            count=Counter.objects.all()
            if count:
                count.get().delete()
            Counter.objects.create(count=0,fine=0)
            count=Counter.objects.get()
            hospitals=Hospital.objects.all()
            schedule=Schedule.objects.all().order_by('doctor_id')
            doctors_active=Doctor.objects.filter(active=True)
            return render(request, 'phcModule/phc_compounder.html',
                          {'days': days, 'users': users, 'count': count,'expired':expired,
                           'stocks': stocks, 'all_complaints': all_complaints,
                           'all_hospitals': all_hospitals, 'hospitals':hospitals, 'all_ambulances': all_ambulances,
                           'appointments_today': appointments_today, 'doctors': doctors,
                           'appointments_future': appointments_future, 'doctors_active': doctors_active, 'schedule': schedule })
    elif usertype == 'student':
        return HttpResponseRedirect("/healthcenter/student")

def student_view(request):
    usertype = ExtraInfo.objects.get(user=request.user).user_type
    if usertype == 'student' or usertype == 'faculty' or usertype == 'staff':
=======
            appointments_today = Appointment.objects.filter(
                date=datetime.now()).order_by('date')
            appointments_future = Appointment.objects.filter(
                date__gt=datetime.now()).order_by('date')
            users = ExtraInfo.objects.filter(user_type='student')
            doctors = Doctor.objects.all()
            inventories = Stockinventory.objects.all().order_by('-date')
            stocks = Stock.objects.all()
            days = Constants.DAYS_OF_WEEK
            schedule = Schedule.objects.all()
            return render(request, 'phcModule/phc_compounder.html',
                          {'inventories': inventories, 'days': days, 'users': users,
                           'stocks': stocks, 'all_complaints': all_complaints,
                           'all_hospitals': all_hospitals, 'all_ambulances': all_ambulances,
                           'appointments_today': appointments_today, 'doctors': doctors,
                           'appointments_future': appointments_future, 'schedule': schedule})
    elif usertype == 'student':
        return HttpResponseRedirect("/healthcenter/student")


def student_view(request):
    usertype = ExtraInfo.objects.get(user=request.user).user_type
    if usertype == 'student':
>>>>>>> da2946e1cfafc8a828075685182d40ebba922cd8
        if request.method == 'POST':
            if 'amb_submit' in request.POST:
                user_id = ExtraInfo.objects.get(user=request.user)
                reason = request.POST.get('reason')
                start_date = request.POST.get('start_date')
                end_date = request.POST.get('end_date')
                if end_date == '':
                    end_date = None
                Ambulance_request.objects.create(
<<<<<<< HEAD
                     user_id=user_id,
                     date_request=datetime.now(),
                     start_date=start_date,
                     end_date=end_date,
                     reason=reason
                 )
=======
                    user_id=user_id,
                    date_request=datetime.now(),
                    start_date=start_date,
                    end_date=end_date,
                    reason=reason
                )
>>>>>>> da2946e1cfafc8a828075685182d40ebba922cd8
                data = {'status': 1}
                return JsonResponse(data)
            elif "appointment" in request.POST:
                user_id = ExtraInfo.objects.get(user=request.user)
                doctor_id = request.POST.get('doctor')
                doctor = Doctor.objects.get(id=doctor_id)
                date = request.POST.get('date')
                schedule = Schedule.objects.get(id=date)
                datei = schedule.date
                description = request.POST.get('description')
                Appointment.objects.create(
                    user_id=user_id,
                    doctor_id=doctor,
                    description=description,
                    schedule=schedule,
                    date=datei
                )
                data = {
<<<<<<< HEAD
                        'status': 1
                        }
=======
                    'status': 1
                }
>>>>>>> da2946e1cfafc8a828075685182d40ebba922cd8
                return JsonResponse(data)
            elif 'doctor' in request.POST:
                doctor_id = request.POST.get('doctor')
                schedule = Schedule.objects.filter(doctor_id=doctor_id)
<<<<<<< HEAD
                days = Schedule.objects.filter(doctor_id=doctor_id).values('day')
=======
                days = Schedule.objects.filter(
                    doctor_id=doctor_id).values('day')
>>>>>>> da2946e1cfafc8a828075685182d40ebba922cd8
                for day in days:
                    for i in range(0, 7):
                        date = (datetime.today()+timedelta(days=i)).date()
                        dayi = date.weekday()
                        d = day.get('day')
                        if dayi == d:
<<<<<<< HEAD
                            Schedule.objects.filter(doctor_id=doctor_id, day=dayi).update(date=date)
=======
                            Schedule.objects.filter(
                                doctor_id=doctor_id, day=dayi).update(date=date)
>>>>>>> da2946e1cfafc8a828075685182d40ebba922cd8
                schedule = Schedule.objects.filter(doctor_id=doctor_id)
                schedules = serializers.serialize('json', schedule)
                return HttpResponse(schedules, content_type='json')
            elif 'feed_submit' in request.POST:
                user_id = ExtraInfo.objects.get(user=request.user)
                feedback = request.POST.get('feedback')
                Complaint.objects.create(
                    user_id=user_id,
                    complaint=feedback,
                    date=datetime.now()
                )
                data = {'status': 1}
                return JsonResponse(data)
        else:
            users = ExtraInfo.objects.all()
            user_id = ExtraInfo.objects.get(user=request.user)
<<<<<<< HEAD
            hospitals = Hospital_admit.objects.filter(user_id=user_id).order_by('-admission_date')
            appointments = Appointment.objects.filter(user_id=user_id).order_by('-date')
            ambulances = Ambulance_request.objects.filter(user_id=user_id).order_by('-date_request')
            prescription = Prescription.objects.filter(user_id=user_id).order_by('-date')
            medicines = Prescribed_medicine.objects.all()
            complaints = Complaint.objects.filter(user_id=user_id).order_by('-date')
            doctors = Doctor.objects.all()
            days = Constants.DAYS_OF_WEEK
            schedule=Schedule.objects.all().order_by('doctor_id')
            doctors_active=Doctor.objects.filter(active=True)
            count=Counter.objects.all()
            if count:
                count.get().delete()
            Counter.objects.create(count=0,fine=0)
            count=Counter.objects.get()

            return render(request, 'phcModule/phc_student.html',
                          {'complaints': complaints, 'medicines': medicines,'doctors_active': doctors_active,
                           'ambulances': ambulances, 'doctors': doctors, 'days': days,'count':count,
=======
            hospitals = Hospital_admit.objects.filter(
                user_id=user_id).order_by('-admission_date')
            appointments = Appointment.objects.filter(
                user_id=user_id).order_by('-date')
            ambulances = Ambulance_request.objects.filter(
                user_id=user_id).order_by('-date_request')
            prescription = Prescription.objects.filter(
                user_id=user_id).order_by('-date')
            medicines = Prescribed_medicine.objects.all()
            schedule = Schedule.objects.all()
            complaints = Complaint.objects.filter(
                user_id=user_id).order_by('-date')
            doctors = Doctor.objects.all()
            days = Constants.DAYS_OF_WEEK

            return render(request, 'phcModule/phc_student.html',
                          {'complaints': complaints, 'medicines': medicines,
                           'ambulances': ambulances, 'doctors': doctors, 'days': days,
>>>>>>> da2946e1cfafc8a828075685182d40ebba922cd8
                           'hospitals': hospitals, 'appointments': appointments,
                           'prescription': prescription, 'schedule': schedule, 'users': users})
    elif usertype == 'compounder':
        return HttpResponseRedirect("/healthcenter/compounder")
