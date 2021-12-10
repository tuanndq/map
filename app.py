import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
# Acquire from developer.here.com
api_key = 'Ax3DtY2b-3EWyh1do9xI2d8tpRq5-gmPIA4D-Mm0d8M'
query = 'hospital'
limit = 5
URL = "https://discover.search.hereapi.com/v1/discover"

@app.route('/', methods=['GET', 'POST'])
def map_func():
    content = request.json
    latitude = content['longtitude'] or 21
    longitude = content['latitude'] or 106

    PARAMS = {
        'apikey': api_key,
        'q': query,
        'limit': limit,
        'at': '{},{}'.format(latitude, longitude)
    }

    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()

    print(data)
    
    result = []
    for i, ele in enumerate(data['items']):
        address = {
            "title": ele['title'],
            "address": ele['address']['label'],
            "latitude": ele['position']['lat'],
            "longitude": ele['position']['lng'],
        }
        result.append(address)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=False)
