#%%
# Import modules
#===============
import pickle
from flask import Flask, request, jsonify


#%%
# General setup
#===============

app = Flask('predict')

with open('model2.bin', 'rb') as m_f, open('dv.bin', 'rb') as t_f:
    model = pickle.load(m_f)
    transformer = pickle.load(t_f)

def get_prediction(customer_data):
    X_data = transformer.transform([customer_data])
    y_pred = model.predict_proba(X_data)[0, 1]
    return float(y_pred)


#%%
# API METHODS
#============

@app.route('/predict', methods=['POST'])
def predict():
    
    customer_data = request.get_json()
    
    prediction = get_prediction(customer_data)

    result = {
        'prediction': prediction
    }
    
    return jsonify(result)


# %%
# RUN IN DEVELOPMENT MODE
#=========================

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)