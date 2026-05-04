import json
import random
import sys
from shapely.geometry import shape, Point
from faker import Faker

def generate_random_point_in_polygon(polygon):
    minx, miny, maxx, maxy = polygon.bounds
    while True:
        p = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
        if polygon.contains(p):
            return p

def main():
    fake = Faker('en_US')
    
    # Load GeoJSON
    with open('KS_CITY_LIMITS_GCS.geojson', 'r') as f:
        geojson_data = json.load(f)
        
    features = geojson_data.get('features', [])
    if not features:
        print("No features found in GeoJSON.")
        sys.exit(1)
        
    # Parse features into shapely shapes
    valid_features = []
    for feature in features:
        geom = feature.get('geometry')
        if geom:
            try:
                poly = shape(geom)
                muni = feature.get('properties', {}).get('MUNI', 'Unknown City')
                valid_features.append({'shape': poly, 'city': muni})
            except Exception as e:
                pass
                
    if not valid_features:
        print("No valid polygons found.")
        sys.exit(1)
        
    dataset = []
    num_points = 10000
    
    for _ in range(num_points):
        # Pick a random feature (city)
        selected = random.choice(valid_features)
        poly = selected['shape']
        city_name = selected['city']
        
        # Generate random point
        pt = generate_random_point_in_polygon(poly)
        
        # Generate fake address components
        street = fake.street_address()
        zip_code = fake.postcode()
        # Random population between 1 and 10 as it's just a single "household" or data point, 
        # or mock a random number up to 500. Let's do 1 to 50
        population = random.randint(1, 50)
        
        doc = {
            "address": {
                "street": street,
                "city": city_name,
                "state": "KS",
                "zip_code": zip_code
            },
            "population": population,
            "location": {
                "type": "Point",
                "coordinates": [round(pt.x, 6), round(pt.y, 6)]
            }
        }
        dataset.append(doc)
        
    with open('dataset.json', 'w') as f:
        json.dump(dataset, f, indent=2)
        
    print(f"Successfully generated {num_points} points in dataset.json")

if __name__ == '__main__':
    main()
