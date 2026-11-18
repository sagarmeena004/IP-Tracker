
import requests
import ipaddress


def find_ip(ip=""):

    # Validate IP Address
    if ip:
        try:
            ipaddress.ip_address(ip)
        except ValueError:
            print("\n[ERROR] Invalid IP Address!")
            return

    # API URL
    if ip:
        url = f"https://ipapi.co/{ip}/json/"
    else:
        url = "https://ipapi.co/json/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        print("\nFetching IP Information...")

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()
        data = response.json()

        if data.get("error"):
            print("\n[ERROR]", data.get("reason", "Invalid IP"))
            return

        # Extract Information
        ip_address = data.get("ip", "N/A")
        city = data.get("city", "N/A")
        region = data.get("region", "N/A")
        country = data.get("country_name", "N/A")
        country_code = data.get("country_code", "N/A")
        latitude = data.get("latitude", "N/A")
        longitude = data.get("longitude", "N/A")
        isp = data.get("org", "N/A")
        postal = data.get("postal", "N/A")
        timezone = data.get("timezone", "N/A")
        version = data.get("version", "N/A")

        # Display Results
        print("\n" + "=" * 45)
        print("          IP ADDRESS TRACKER")
        print("=" * 45)

        print(f"IP Address     : {ip_address}")
        print(f"IP Version     : {version}")
        print(f"City           : {city}")
        print(f"Region         : {region}")
        print(f"Country        : {country}")
        print(f"Country Code   : {country_code}")
        print(f"Postal Code    : {postal}")
        print(f"Timezone       : {timezone}")
        print(f"ISP / Network  : {isp}")
        print(f"Latitude       : {latitude}")
        print(f"Longitude      : {longitude}")

        # Google Maps Link
        if latitude != "N/A" and longitude != "N/A":
            maps_link = (
                f"https://www.google.com/maps?q={latitude},{longitude}"
            )

            print("\nGoogle Maps Location:")
            print(maps_link)

        print("=" * 45)
        print("       IP SEARCH COMPLETED")
        print("=" * 45)

    except requests.Timeout:
        print("\n[ERROR] Request Timed Out!")

    except requests.ConnectionError:
        print("\n[ERROR] Check Your Internet Connection!")

    except requests.HTTPError as e:
        print("\n[ERROR] HTTP Error:", e)

    except requests.RequestException as e:
        print("\n[ERROR] Request Failed:", e)

    except ValueError:
        print("\n[ERROR] Invalid API Response!")


# Main Program
print("=" * 45)
print("          PYTHON IP TRACKER")
print("=" * 45)

ip = input("\nEnter IP Address (Leave Empty for Your IP): ").strip()

find_ip(ip)
