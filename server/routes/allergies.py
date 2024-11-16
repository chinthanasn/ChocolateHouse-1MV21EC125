from flask import Blueprint, request, jsonify
from db_manager import get_connection

allergiesBP = Blueprint("allergies", __name__)

@allergiesBP.route("/", methods=["GET"])
def get_allergies():

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT customer_name, allergy, suggestion FROM allergies")
    allergies = cursor.fetchall()
    connection.close()

    result = [{"customer_name": row[0], "allergy": row[1], "suggestion": row[2]} for row in allergies]
    return jsonify(result)

@allergiesBP.route("/", methods=["POST"])
def add_allergy():

    try:
        data = request.json
        customer_name = data.get("customer_name")
        allergy = data.get("allergy")
        suggestion = data.get("suggestion")

        if not customer_name or not allergy or not suggestion:
            return jsonify({"error": "Customer name, allergy, and suggestion are required"}), 400

        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO allergies (customer_name, allergy, suggestion) VALUES (?, ?, ?)",
            (customer_name, allergy, suggestion),
        )
        connection.commit()
        connection.close()
        return jsonify({"message": "Allergy added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@allergiesBP.route("/<customer_name>", methods=["GET"])
def get_allergies_by_customer(customer_name):

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT allergy, suggestion FROM allergies WHERE customer_name = ?", (customer_name,))
    allergies = cursor.fetchall()
    connection.close()

    if not allergies:
        return jsonify({"message": f"No allergies found for customer {customer_name}"}), 404

    result = [{"allergy": row[0], "suggestion": row[1]} for row in allergies]
    return jsonify(result)
