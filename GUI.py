import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np

# Load the saved model
model = joblib.load('best_model.pkl')

def predict():
    try:
        # Get input values from entry widgets
        followers = int(entry_followers.get())
        following = int(entry_following.get())
        posts = int(entry_posts.get())
        bio_length = int(entry_bio_length.get())
        username = 0  # Dummy value, we skipped username in input

        # Prepare input data
        input_data = np.array([[username, followers, following, posts, bio_length]])

        # Predict
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            messagebox.showinfo("Result", "⚠️ Fake Profile Detected!")
        else:
            messagebox.showinfo("Result", "✅ Real Profile Detected!")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create GUI window
root = tk.Tk()
root.title("Fake Profile Detection")
root.geometry("300x300")

# Input fields
tk.Label(root, text="Followers:").pack()
entry_followers = tk.Entry(root)
entry_followers.pack()

tk.Label(root, text="Following:").pack()
entry_following = tk.Entry(root)
entry_following.pack()

tk.Label(root, text="Posts:").pack()
entry_posts = tk.Entry(root)
entry_posts.pack()

tk.Label(root, text="Bio Length:").pack()
entry_bio_length = tk.Entry(root)
entry_bio_length.pack()

# Predict button
predict_button = tk.Button(root, text="Check Profile", command=predict)
predict_button.pack(pady=10)

root.mainloop()