from flask import *
import pymongo, os

app = Flask(__name__)

# myclient = pymongo.MongoClient("mongodb://13.59.213.80:27017/",
#                             username='candles123',
#                             password='D1}d-0oMe[Ts8f>OPcjH,aiC',
#                             authSource='admin',
#                             connect=False)

myclient = pymongo.MongoClient("mongodb://localhost:27017/",
                            connect=False)

MYDB = myclient['ballarpur']
VILLAGESCOLL = MYDB['villages_d']

@app.route('/village_data', methods = ['GET'])
def village_data():

    if 'location_id' in request.args:
        location_id = request.args['location_id']
        print(location_id)

        data = VILLAGESCOLL.find_one({'location_id': str(location_id)}, {"_id": 0})

        js = json.dumps(data)

        resp = Response(js)
        resp.headers.add('Access-Control-Allow-Origin', '*')

        return resp


port = int(os.environ.get('PORT', 8001))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port)
