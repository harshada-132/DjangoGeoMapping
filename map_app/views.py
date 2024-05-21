from django.shortcuts import render
import os
import json

def index(request):
    # Define the path to the GeoJSON file
    file_path = os.path.join(os.path.dirname(__file__), '/home/harshada/Desktop/Village Map/village_map/Pune_prj 1.geojson')
    
    # Open and read the GeoJSON file
    with open(file_path) as f:
        village_data = json.load(f)
    
    # Extract village information from the GeoJSON data
    villages = [
        {
            'name': feature['properties']['Village'],
            'lat': feature['geometry']['coordinates'][0][0][1],  # Assuming the first coordinate for simplicity
            'lng': feature['geometry']['coordinates'][0][0][0],
            'district': feature['properties']['District']
        }
        for feature in village_data['features']
    ]

    # Pass the extracted village data to the template
    return render(request, 'index.html', {'villages': json.dumps(villages)})
