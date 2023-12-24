# src/api/model_endpoints.py

from flask import Flask, request, jsonify
import src.models.model_trainer as model_trainer
import src.models.model_predictor as model_predictor
import src.database.data_connector as data_connector
import src.utils.validation as validation

app = Flask(__name__)

@app.route('/train', methods=['POST'])
def train_model():
    try:
        # Retrieve and validate input data
        input_data = request.get_json()
        validation.validate_training_data(input_data)
        
        # Train the model using the input data
        trained_model = model_trainer.train_model(input_data)
        
        # Return the trained model parameters or other relevant response
        return jsonify({'message': 'Model trained successfully', 'model_params': trained_model.params})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve and validate input data
        input_data = request.get_json()
        validation.validate_prediction_data(input_data)
        
        # Make predictions using a trained model
        predictions = model_predictor.predict(input_data)
        
        # Return the predictions or other relevant response
        return jsonify({'predictions': predictions})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/retrieve_data', methods=['GET'])
def retrieve_data():
    try:
        # Retrieve data from the database
        data = data_connector.retrieve_data()
        
        # Return the retrieved data or other relevant response
        return jsonify({'data': data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

