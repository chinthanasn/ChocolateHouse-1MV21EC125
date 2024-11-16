from flask import Blueprint, request, jsonify
from flask_cors import CORS
import sqlite3

flavoursBP = Blueprint("flavours", __name__)
CORS(flavoursBP, supports_credentials=True)

DB_PATH = "choco.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

@flavoursBP.route("/", methods=["GET"])
def get_flavours():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT name, season, availability FROM flavours")
    flavours = cursor.fetchall()
    connection.close()
    result = [{"name": row[0], "season": row[1], "availability": bool(row[2])} for row in flavours]
    return jsonify(result)

@flavoursBP.route("/", methods=["POST"])
def add_flavour():
    try:
        data = request.json
        name = data.get("name")
        season = data.get("season")
        availability = data.get("availability")

        if not name or not season:
            return jsonify({"error": "Name and season are required"}), 400

        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO flavours (name, season, availability) VALUES (?, ?, ?)", 
                       (name, season, availability))
        connection.commit()
        connection.close()
        return jsonify({"message": "Flavour added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
