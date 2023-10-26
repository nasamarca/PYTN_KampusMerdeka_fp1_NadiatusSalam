from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained machine learning model
model = joblib.load('D:\\01-Universitas Diponegoro\\01-Informatics\\Semester 7\\Hacktiv8\\H8_5_PYTN-KS19-014\\PYTN_KampusMerdeka_fp1_NadiatusSalam\\Flask\\PYTN_KampusMerdeka_fp1_NadiatusSalam.pkl')

@app.route('/', methods=['GET', 'POST'])
def predict_price():
    prediction_result = None
    if request.method == 'POST':
        # Extract input data from the form
        name_cab = 'Lyft XL'
        distance = float(2.94)
        surge_multiplier = float(0.0)
        
        # Prepare the input data for prediction
        new_data = [[name_cab,distance, surge_multiplier]]

        # Perform prediction
        predicted_price = model.predict(new_data)[0]
        prediction_result = round(predicted_price, 2)

    return  prediction_result

if __name__ == '__main__':
    app.run(debug=True)