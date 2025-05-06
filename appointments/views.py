from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import AppointmentForm
from .whatsapp_utils import send_whatsapp_text, send_whatsapp_image, send_whatsapp_location
from django.core.mail import send_mail

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()  # Saving appointment into database

            send_mail(
                'Appointment Confirmed!',
                f'Thank you {appointment.name} for booking {appointment.service} on {appointment.date} at {appointment.time}. See you soon!',
                'gmallik1011@gmail.com',  # replace with your Gmail
                [appointment.email, 'gmallik1011@gmail.com'],  # sends to user and you
                fail_silently=False,
            )

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
            try:
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
                print("WhatsApp Error:", e)

            return redirect('thank_you')
        else:
            # Return form errors as JSON if the form is invalid
            return JsonResponse(form.errors, status=400)
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book_appointment.html', {'form': form})


def thank_you(request):
    return render(request, 'appointments/thank_you.html')