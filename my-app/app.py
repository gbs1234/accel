from flask import Flask, request, jsonify, render_template 
import joblib
import pandas as pd
import os
import zipfile
from collections import Counter


def make_windows(df, category='unknown'):
    '''
    WThis function calculates the features from a CSV file. 
    There will be 10 features for each window of time. 
    
    df: pandas DataFrame
    category: string
    '''

    dt = df.time.max()/(len(df) - 1)
    window_size = 2   # size of the windows
    samples_per_window = int(window_size/dt)
    
    features = []  # list of features. There will be 10 features. 
    
    for start in range(0, len(df), samples_per_window):
        window = df.iloc[start:start+samples_per_window]
        if len(window) < samples_per_window:
            continue  # ignora se a última janela ficar incompleta
    
            # Calcula atributos simples
        mean_x = window['ax'].mean()
        std_x  = window['ax'].std()
        amp_x  = window['ax'].max() - window['ax'].min()
        mean_y = window['ay'].mean()
        std_y  = window['ay'].std()
        amp_y  = window['ay'].max() - window['ay'].min()
        mean_z = window['az'].mean()
        std_z  = window['az'].std()
        amp_z  = window['az'].max() - window['az'].min()
        m_abs  = window['abs'].mean()  # média da aceleração absoluta
    
        features.append({
            'mean_x': mean_x, 'std_x': std_x, 'amp_x': amp_x,
            'mean_y': mean_y, 'std_y': std_y, 'amp_y': amp_y,
            'mean_z': mean_z, 'std_z': std_z, 'amp_z': amp_z,
            'm_abs' : m_abs, 
            'classe': category  
        })
    
    # Retornamos os atributos na forma de um dicionário
    return pd.DataFrame(features)




# Initialize the Flask app
app = Flask(__name__)

LABEL_TO_EMOJI = {
    "steady": "🧍",
    "walk": "🚶",
    "run": "🏃",
    "dance": "💃",
}



# Load the trained model
try:
    with open('knn_model.joblib', 'rb') as model_file:
        model = joblib.load(model_file)
except FileNotFoundError:
    print("Error: model.pkl not found. Make sure you've saved your model.")
    model = None


# Define the prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500

    # Get the data from the user request
    file = request.files['uploaded_file']  #load zip
    
    filename = file.filename
    custom_names = ['time', 'ax', 'ay', 'az', 'abs']
    
    # Detect file type by extension
    ext = os.path.splitext(filename)[-1].lower()
    
    

    if ext in [".zip"]:
        with zipfile.ZipFile(file) as z:
            with z.open("Raw Data.csv") as f:
                df = pd.read_csv(f, header=0, names=custom_names)  
                
    elif ext in [".csv"]:
        df = pd.read_csv(file, header=0, names=custom_names) 
    else:
        return {"error": f"Unsupported file type: {ext}"}, 400

    # Ensure dataframe is not empty
    if df.empty:
        return {"error": "Uploaded file is empty"}, 400
    
    
    
    

    #pd_data = pd.read_csv(data_file, header=0, names=custom_names)
    
    df_windows = make_windows(df) 
    X = df_windows.drop('classe', axis = 1)
    

    # Make a prediction
    predictions = model.predict(X)  # There is a result for each row of X
    
      
    
    results = []
    for i, label in enumerate(predictions):
        results.append({
            "time": i * 2,                     # segundos
            "label": label,
            "emoji": LABEL_TO_EMOJI.get(label, "❓"),
        })

    
   # 4. resumo (quantos "walk", "dance", etc)
    counts = Counter(predictions)

    # Return the result
    return render_template(
        "results.html",
        results=results,
        counts=counts,
        total=len(predictions),
    )



@app.route("/")
def home():
    return open("index.html").read()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
    
