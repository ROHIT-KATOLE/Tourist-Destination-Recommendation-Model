import pandas as pd
from flask import Flask, request, jsonify
from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import NearestNeighbors
from geopy.geocoders import Nominatim
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

places_data = pd.read_csv('Project_website - Sheet1.csv')

encoder = OneHotEncoder()
category_encoded = encoder.fit_transform(places_data[['Category']])

features = pd.concat([places_data[['Latitude', 'Longitude']], pd.DataFrame(category_encoded.toarray())], axis=1)
features.columns = features.columns.astype(str)

k = 3
knn_model = NearestNeighbors(n_neighbors=k, metric='euclidean')
knn_model.fit(features)

def get_lat_long(location):
    geolocator = Nominatim(user_agent="geoapiExercise")
    location_info = geolocator.geocode(location)
    if location_info:
        return location_info.latitude, location_info.longitude
    else:
        return None, None

def recommend_places(location, category):
    latitude, longitude = get_lat_long(location)
    if latitude is None or longitude is None:
        print(f"Could not determine coordinates for {location}.")
        return None

    input_features = encoder.transform(pd.DataFrame([[category]]))
    input_location = pd.DataFrame([[latitude, longitude]], columns=['Latitude', 'Longitude'])
    category_columns = encoder.get_feature_names_out(['Category'])

    input_features = pd.concat([input_location, pd.DataFrame(input_features.toarray(), columns=category_columns)], axis=1)
    input_features.columns = features.columns
    _, indices = knn_model.kneighbors(input_features, n_neighbors=k)

    recommended_places = places_data.iloc[indices[0]]

    return recommended_places

@app.route('/recommend', methods=['POST', 'OPTIONS'])
def recommend():
    if request.method == 'OPTIONS':
        # This is an OPTIONS request, respond with the allowed methods and headers
        response = app.make_default_options_response()
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response

    # This is a POST request, process the data and respond accordingly
    data = request.get_json()
    location = data.get('location')  # Use get to handle missing keys gracefully
    category = data.get('category')

    if location is None or category is None:
        # Handle missing or incorrect data
        return jsonify({'error': 'Invalid data. Location and category are required.'}), 400

    recommendations = recommend_places(location, category)

    if recommendations is None:
        return jsonify({'error': 'Could not determine recommendations.'}), 500

    # Returning the recommendations as JSON
    return jsonify({'recommendations': recommendations.to_dict(orient='records')})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
