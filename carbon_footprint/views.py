# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    if request.method == 'POST':
        num_house = int(request.POST['num_house'])
        num_of_industries = int(request.POST['num_of_industries'])
        num_of_vehicle = int(request.POST['num_of_vehicle'])
        water_surface_area = float(request.POST['water_surface_area'])
        water_volume = float(request.POST['water_volume'])

        # Calculate carbon emissions from household
        household_carbon_emissions = 48 * num_house
        
        # Calculate carbon emissions from industry
        industry_carbon_emissions = 51958.433 * num_of_industries
        
        # Calculate carbon emissions from vehicle
        vehicle_carbon_emissions = 4.6 * num_of_vehicle 
        
        # Calculate carbon emissions from water bodies
        water_bodies_carbon_emissions = water_surface_area * water_volume * 2.7 * 10 ** -7

        # Calculate total carbon footprint
        total_carbon_footprint = household_carbon_emissions + industry_carbon_emissions + vehicle_carbon_emissions + water_bodies_carbon_emissions
        
        return render(request, 'home.html',{'total_carbon_footprint': total_carbon_footprint})

    return render(request, 'home.html')