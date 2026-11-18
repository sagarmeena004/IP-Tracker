import requests

def find_ip(ip=""):
    url = f"https://ipapi.co/{ip}/json/"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url,headers=headers, timeout=10)
        data = response.json()

        if "error" in data:
            print("Invalid IP address!")
            return
        print("\n--- IP Address Details ---")
        print("IP Address:",data.get("ip"))
        print("City:", data.get("city"))
        print("Region:",data.get("region"))
        print("Country:",data.get("country_name"))
        print("Latitude:",data.get("latitude"))
        print("Longitude:",data.get("longitude"))
        print("ISP:",data.get("org"))

    except requests.RequestException:
        print("Unable to connect to the server.")

ip = input("Enter IP Address (leave empty for your IP) :")
find_ip(ip)