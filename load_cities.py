import os
import json
import re
from pymongo import MongoClient
from dotenv import load_dotenv

def to_camel_case(text):
    if text == "OBJECTID":
        return "objectId"
        
    parts = [p for p in re.split(r'_+', text) if p]
    if not parts:
        return text
        
    first = parts[0].lower()
    rest = [p.capitalize() for p in parts[1:]]
    return first + "".join(rest)

def main():
    load_dotenv()
    
    mongodb_uri = os.getenv("MONGODB_URI")
    if not mongodb_uri:
        print("Error: MONGODB_URI not found in .env file.")
        return
        
    client = MongoClient(mongodb_uri)
    db = client['gerrymander']
    collection = db['city_limits']
    
    # Clear existing collection if we want a fresh start
    collection.delete_many({})
    
    print("Reading KS_CITY_LIMITS_GCS.geojson...")
    with open("KS_CITY_LIMITS_GCS.geojson", "r") as f:
        data = json.load(f)
        
    features = data.get("features", [])
    if not features:
        print("No features found in the GeoJSON.")
        return
        
    documents_to_insert = []
    
    for feature in features:
        original_props = feature.get("properties", {})
        camel_case_props = {to_camel_case(k): v for k, v in original_props.items()}
        
        doc = {
            "geometry": feature.get("geometry", {})
        }
        doc.update(camel_case_props)
        
        documents_to_insert.append(doc)
        
    if documents_to_insert:
        print(f"Inserting {len(documents_to_insert)} documents into MongoDB...")
        result = collection.insert_many(documents_to_insert)
        print(f"Successfully inserted {len(result.inserted_ids)} documents into the 'city_limits' collection.")
    else:
        print("No documents to insert.")

if __name__ == "__main__":
    main()
