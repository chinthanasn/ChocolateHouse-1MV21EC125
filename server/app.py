from flask import Flask
from flask_cors import CORS
from db_manager import initialize_database
from routes.flavours import flavoursBP
from routes.inventory import inventoryBP
from routes.allergies import allergiesBP

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})  #CORS allow

app.register_blueprint(flavoursBP, url_prefix="/flavours")
app.register_blueprint(inventoryBP, url_prefix="/inventory")
app.register_blueprint(allergiesBP, url_prefix="/allergies")

initialize_database() 

if __name__ == '__main__':
    app.run(debug=True)
