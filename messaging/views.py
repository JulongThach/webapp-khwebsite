from django.shortcuts import render, redirect
import requests
from django.contrib import messages
from .forms import MessageForm

# Replace with your Telegram Bot Token and Chat ID
BOT_TOKEN = "7808231868:AAHNf2dvyAm697DyB2wfLlrUS-PpniK29YI"
CHAT_ID = "-4770597616"

def send_telegram_message(name, phone, subject, message):
    text = f"📩 *New Message Received*\n\n👤 Name: {name}\n📱 Phone Number: {phone}\n📕 Subject: {subject}\n💬 Message: {message}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

def send_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            phone = form.cleaned_data["phone"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            send_telegram_message(name, phone, subject, message)
            messages.success(request, 'Message Send')
            return render(request, "messaging/contact.html", {"form": form})  # Redirect after successful submission
    else:
        form = MessageForm()
        
    return render(request, "messaging/contact.html", {"form": form})

def home(request):
    return render(request, "messaging/index.html")

def success(request):
    return render(request, "messaging/success.html")
