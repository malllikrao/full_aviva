import requests

# ✅ Your UltraMsg API credentials
instance_id = "instance117060"
token = "5i4kzjch71bmfoqi"

def send_whatsapp_text(to, message):
    url = f"https://api.ultramsg.com/{instance_id}/messages/chat"
    data = {
        "token": token,
        "to": to,
        "body": message
    }
    requests.post(url, data=data)

def send_whatsapp_image(to, image_url, caption=""):
    url = f"https://api.ultramsg.com/instance117060/messages/image"
    data = {
        "token": "5i4kzjch71bmfoqi",
        "to": to,
        "image": image_url,
        "caption": caption
    }
    response = requests.post(url, data=data)
    
    # 🔍 DEBUG: print UltraMsg response
    print("WhatsApp Image Send Response:", response.status_code, response.json())
def send_whatsapp_location(to, latitude, longitude, address=""):
    url = f"https://api.ultramsg.com/{instance_id}/messages/location"
    data = {
        "token": token,
        "to": to,
        "latitude": latitude,
        "longitude": longitude,
        "address": address
    }
    requests.post(url, data=data)

    
