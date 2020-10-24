from django.shortcuts import render
import json
import requests

# Create your views here.
#https://api.waqi.info/feed/hyderabad/?token=daee0bdc5082ab8418e342613fe314cac0955a5f
def index(request):
    if request.method == "POST" :
        city_name = request.POST['tbCityName']
        api_request = requests.get('https://api.waqi.info/feed/' + city_name +'/?token=daee0bdc5082ab8418e342613fe314cac0955a5f')

        try:
            api_data = json.loads(api_request.content)
        except Exception as e:
            api_data = "Error in loading data"

        if api_data['data']['aqi'] <= 50 :
            category_description = 'Air quality is satisfactory, and air pollution poses little or no risk.'
            category_color = "good"
        elif api_data['data']['aqi'] >= 51 and api_data['data']['aqi'] <= 100 :
            category_description = "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif api_data['data']['aqi'] >= 101 and api_data['data']['aqi'] <= 150 : 
            category_description = "Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            category_color = "usg"
        elif api_data['data']['aqi'] >= 151 and api_data['data']['aqi'] <= 200 :
            category_description = "Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api_data['data']['aqi'] >= 201 and api_data['data']['aqi'] <= 300 :
            category_description = "Health alert: The risk of health effects is increased for everyone."
            category_color = "veryunhealthy"
        elif api_data['data']['aqi'] >= 301 :
            category_description = "Health warning of emergency conditions: everyone is more likely to be affected."
            category_color = "hazardous"

        context = {'api_data' : api_data, 'category_description' : category_description, 'category_color' : category_color}
        return render(request, 'airquality/index.html', context)
    
    else : 
        api_request = requests.get('https://api.waqi.info/feed/delhi/?token=daee0bdc5082ab8418e342613fe314cac0955a5f')

        try:
            api_data = json.loads(api_request.content)
        except Exception as e:
            api_data = "Error in loading data"

        if api_data['data']['aqi'] <= 50 :
            category_description = 'Air quality is satisfactory, and air pollution poses little or no risk.'
            category_color = "good"
        elif api_data['data']['aqi'] >= 51 and api_data['data']['aqi'] <= 100 :
            category_description = "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif api_data['data']['aqi'] >= 101 and api_data['data']['aqi'] <= 150 : 
            category_description = "Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            category_color = "usg"
        elif api_data['data']['aqi'] >= 151 and api_data['data']['aqi'] <= 200 :
            category_description = "Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api_data['data']['aqi'] >= 201 and api_data['data']['aqi'] <= 300 :
            category_description = "Health alert: The risk of health effects is increased for everyone."
            category_color = "veryunhealthy"
        elif api_data['data']['aqi'] >= 301 :
            category_description = "Health warning of emergency conditions: everyone is more likely to be affected."
            category_color = "hazardous"

        context = {'api_data' : api_data, 'category_description' : category_description, 'category_color' : category_color}
        return render(request, 'airquality/index.html', context)

def about(request):
    return render(request, 'airquality/about.html')

def aqi(request):
    return render(request, 'airquality/aqi.html')