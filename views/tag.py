from flask import request, jsonify

from flask import current_app as app

@app.route("/tag/test", methods=["GET"])
def test_method():
    return jsonify({"message" : "Success~!"}), 201