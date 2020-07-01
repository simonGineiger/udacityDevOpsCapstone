from flask import Flask, request
from flask_cors import CORS
import fromPostgres

app = Flask(__name__)
CORS(app, resources=r'/ingest/*')


def pairings_default():
    return "[\"ETHUSD\", \"BTCUSD\", \"XLMUSD\", \"XRPUSD\"]"


@app.route("/XCL/getStats", methods=["GET", "OPTIONS"])
def get_latest_statistics():
    timeframe = int(request.args.get("timeframe", "1440"))  # default timeframe 24 hours
    pairings = request.args.get("pairings", pairings_default()).strip("][").split(", ")
    result = fromPostgres.get_latest(pairings, timeframe_in_minutes=timeframe, stats=True)
    return result


@app.route("/XCL/getLatest", methods=["GET", "OPTIONS"])
def get_latest_ohlcv_data():
    timeframe = int(request.args.get("timeframe", "180"))
    pairings = request.args.get("pairings", pairings_default()).strip("][").split(", ")
    result = fromPostgres.get_latest(pairings, timeframe_in_minutes=timeframe)
    return result


@app.route("/XCL/getDamaged", methods=["GET", "OPTIONS"])
def get_damaged_ohlcv_data():
    pairings = request.args.get("pairings", pairings_default()).strip("][").split(", ")
    mend_only = request.args.get("mend_only", False)
    result = fromPostgres.get_damaged(pairings=pairings, mend_only=mend_only)
    return result


@app.before_request
def before_request_func():
    print("before_request is running")


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


app.run(host='0.0.0.0', port=80)
