from flask import Blueprint, request, jsonify
from flask_cors import CORS
import sqlite3

inventoryBP = Blueprint("inventory", __name__)
CORS(inventoryBP, supports_credentials=True)

DB_PATH = "choco.db"

def get_connection():
    """Establish and return a connection to the database."""
    return sqlite3.connect(DB_PATH)

@inventoryBP.route("/", methods=["GET"])
def get_inventory():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT ingredient, quantity, availability FROM inventory")
    inventory = cursor.fetchall()
    connection.close()
    result = [{"ingredient": row[0], "quantity": row[1], "availability": bool(row[2])} for row in inventory]
    return jsonify(result)

@inventoryBP.route("/", methods=["POST"])
def add_inventory():
    try:
        data = request.json
        ingredient = data.get("ingredient")
        quantity = data.get("quantity")
        availability = data.get("availability")

        if not ingredient or not quantity:
            return jsonify({"error": "Ingredient and quantity are required"}), 400

        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO inventory (ingredient, quantity, availability) VALUES (?, ?, ?)", 
                       (ingredient, quantity, availability))
        connection.commit()
        connection.close()
        return jsonify({"message": "Inventory item added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
