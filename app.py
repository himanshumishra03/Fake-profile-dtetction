from flask import Flask, render_template, request
import numpy as np
import joblib  # or pickle, depending on how you saved your model

app = Flask(__name__)

# Load your trained model
model = joblib.load('best_model.pkl')  # update this as needed

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        username = request.form['username']
        num_followers = int(request.form['num_followers'])
        num_following = int(request.form['num_following'])
        account_age_days = int(request.form['account_age_days'])
        posts_count = int(request.form['posts_count'])

        # Feature extraction from username
        username_length = len(username)

        # Prepare the features as an array
        features = np.array([[username_length, num_followers, num_following, account_age_days, posts_count]])

        # Make prediction
        prediction = model.predict(features)[0]

        # Convert prediction to human-readable text
        result = "Fake Profile 🚨" if prediction == 1 else "Genuine Profile ✅"

        return render_template('index.html', prediction=result)

    except Exception as e:
        return render_template('index.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)