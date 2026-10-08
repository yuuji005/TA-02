from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__, template_folder='Template')

# Memuat model
model = joblib.load('Model/model.joblib')

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_text = None
    rating_input = None
    prediction_val = None

    if request.method == 'POST':
        try:
            # Mengambil input rating dari formulir web
            rating_input = float(request.form['rating'].replace(',', '.'))
            
            # Melakukan prediksi menggunakan model
            input_data = np.array([[rating_input]])
            pred = model.predict(input_data)[0]
            prediction_val = round(float(pred))
            prediction_text = f"{prediction_val:,}".replace(',', '.')
        except Exception as e:
            prediction_text = "Error saat memproses data"

    return render_template('index.html', 
                           prediction_text=prediction_text, 
                           rating_input=rating_input,
                           prediction_val=prediction_val)

if __name__ == '__main__':
    app.run(debug=True)