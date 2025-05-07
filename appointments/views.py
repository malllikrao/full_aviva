import threading  # Add this import at the top
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import AppointmentForm
from .whatsapp_utils import send_whatsapp_text, send_whatsapp_image, send_whatsapp_location
from django.core.mail import send_mail
from django.views.decorators.http import require_http_methods
import json

@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'message': 'CSRF cookie set'})

def send_notifications(appointment):
    # Send email
    try:
        send_mail(
            'Appointment Confirmed!',
            f'Thank you {appointment.name} for booking {appointment.service} on {appointment.date} at {appointment.time}. See you soon!',
            'gmallik1011@gmail.com',
            [appointment.email, 'gmallik1011@gmail.com'],
            fail_silently=False,
        )
    except Exception as e:
        print("❌ Email Error:", e)

    # Send WhatsApp messages
    try:
        user_phone = appointment.phone.replace("+", "").replace(" ", "")
        message = f"""
Hi {appointment.name}, thank you for booking your {appointment.service} on {appointment.date} at {appointment.time}. See you soon! at Aviva Aesthetics! 💆‍♀️

📍 Clinic: Aviva Aesthetics
🧑‍⚕️ Dr. Haripriya
📞 +91 99206 09900
📌 Address: Biba Showroom , Near to Court chowrasta , Karimnagar
📍 Maps: https://g.co/kgs/2hFGkMg
🕐 Timings: Mon–Sat, 10:00 AM – 7:30 PM

See you soon! ✨
"""
        send_whatsapp_text(user_phone, message)
        send_whatsapp_image(
            user_phone,
            "https://i.postimg.cc/3RhcJbTB/dr-hari-priya-aviva-aesthetics-christian-colony-karimnagar-dermatologists-di15p5bj0s.jpg",
            "Welcome to Aviva Aesthetics 💆‍♀️"
        )
        send_whatsapp_location(
            user_phone,
            17.459720,
            78.500305,
            "Aviva Aesthetics Clinic, Secunderabad"
        )
    except Exception as e:
        print("❌ WhatsApp Error:", e)

@ensure_csrf_cookie
@require_http_methods(["GET", "POST"])
def book_appointment(request):
    if request.method == 'POST':
        # JSON request (from frontend)
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body.decode('utf-8'))
                print("✅ Received JSON data:", data)
                form = AppointmentForm(data)
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON'}, status=400)
        else:
            form = AppointmentForm(request.POST)

        if form.is_valid():
            appointment = form.save()

            # ✅ Run email + WhatsApp logic in a separate thread
            threading.Thread(target=send_notifications, args=(appointment,)).start()

            if request.content_type == 'application/json':
                return JsonResponse({'message': 'Appointment successfully booked!'})
            else:
                return redirect('thank_you')
        else:
            print("❌ Form Errors:", form.errors)
            return JsonResponse(form.errors, status=400)

    # For GET requests
    form = AppointmentForm()
    return render(request, 'appointments/book_appointment.html', {'form': form})

def thank_you(request):
    return render(request, 'appointments/thank_you.html')


