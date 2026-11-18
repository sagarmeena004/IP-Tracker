
# Project Documentation

## 1. Project Overview

Python IP Address Tracker is a command-line application that retrieves public IP address information through the IPAPI service.

## 2. Project Objectives

- Understand Python API integration.
- Learn HTTP requests.
- Validate IPv4 and IPv6 addresses.
- Extract JSON response data.
- Handle network and API errors.

## 3. Working Process

1. User enters an IP address.
2. Python validates the address.
3. Application sends an HTTP request.
4. IPAPI returns JSON information.
5. Application extracts relevant details.
6. Results are displayed in the terminal.

## 4. Basic Version

The final.py file provides basic IP information, including city, region, country, coordinates, and ISP.

## 5. Advanced Version

The gpt.py file includes:

- IP validation
- IP version detection
- Country code
- Postal code
- Timezone
- Google Maps link
- Detailed exception handling

## 6. Python Libraries

- requests
- ipaddress

The ipaddress module is included in Python's standard library.

## 7. API Information

API Provider: IPAPI

API Endpoint: https://ipapi.co/

## 8. Limitations

- Requires an internet connection.
- API availability and usage limits apply.
- IP location is approximate.
- VPNs and proxies may affect location results.
- Does not provide exact GPS tracking.

## 9. Conclusion

This project demonstrates practical Python programming, API integration, data extraction, and exception handling.
