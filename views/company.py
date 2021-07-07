from flask import request, jsonify

from flask import current_app as app

@app.route("/company/test", methods=["GET"])
def test_method():
    return jsonify({"message" : "Success~!"}), 201