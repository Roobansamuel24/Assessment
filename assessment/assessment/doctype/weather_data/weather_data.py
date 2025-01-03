# Copyright (c) 2025, Rooban Samuel and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import requests
from datetime import datetime

class WeatherData(Document):
	pass

@frappe.whitelist()
def fetch_weather_data(city_name):
  
    api_url = "https://api.weatherstack.com/current"
    access_key = "7b312c40c857b3bb83cf51a5ddae22be"

    params = {
        "access_key": access_key,
        "query": city_name
    }

    try:
        response = requests.get(api_url, params=params)
        data = response.json()

        if "error" in data:
            frappe.throw(f"Error: {data['error']['info']}")

        location = data.get("location", {})
        current = data.get("current", {})

        weather_doc = frappe.new_doc("Weather Data")
        weather_doc.city = location.get("name")
        weather_doc.temperature = current.get("temperature")
        weather_doc.pressure = current.get("pressure")
        weather_doc.windspeed = current.get("wind_speed")
        weather_doc.humidity = current.get("humidity")
        weather_doc.weather_description = ", ".join(current.get("weather_descriptions", []))

        localtime_str = location.get("localtime") 
        if localtime_str:
            parsed_time = datetime.strptime(localtime_str, "%Y-%m-%d %H:%M")
            formatted_time = parsed_time.strftime("%Y-%m-%d %H:%M:%S")
            weather_doc.timestamp = formatted_time

        weather_doc.insert(ignore_permissions=True)
        frappe.db.commit()

        return {"status": "success", "message": f"Weather data for {city_name} saved successfully."}

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Weather Data Fetch Error")
        frappe.throw(f"An error occurred: {str(e)}")
