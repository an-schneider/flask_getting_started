from flask import Flask, jsonify, request

app = Flask(__name__)

my_name = {"name": "Anthony Schneider"}

@app.route("/name", methods=["GET"])
def name():
    return jsonify(my_name)


@app.route("/hello/name", methods=["GET"])
def message():
    """
    Returns the data dictionary below to the caller as JSON
    """
    my_message = {
        "message": "Hello there, %s" % my_name["name"]
    }

    return jsonify(my_message)


@app.route("/distance", methods=["POST"])
def distance():
    r = request.get_json()

    point_a = r["a"]
    point_b = r["b"]

    xa = point_a[0]
    xb = point_b[0]
    ya = point_a[1]
    yb = point_b[1]

    xdis = abs(xa-xb)
    ydis = abs(ya-yb)

    total_distance = (xdis + ydis)**(1/2)
    result = {"distance": total_distance,
              "a": point_a,
              "b": point_b}

    return jsonify(result)

