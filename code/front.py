import tkinter as tk
from tkinter import messagebox
import pickle

# Load the data and similarity matrix
new = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function to recommend movies
def recommend_movie():
    movie = entry.get()
    if movie not in new['title'].values:
        messagebox.showerror("Error", "Movie not found in database!")
        return
    index = new[new['title'] == movie].index[0]
    distances = sorted(enumerate(similarity[index]), key=lambda x: x[1], reverse=True)
    recommended_movies = [new.iloc[i[0]].title for i in distances[1:6]]

    # Update the result label
    result_text = "\n".join(recommended_movies)
    result_label.config(text=f"Recommended Movies:\n{result_text}")

# Create the main application window
root = tk.Tk()
root.title("Movie Recommendation System")
root.geometry("500x400")
root.configure(bg="black")  # Set background to black

# Heading label
heading = tk.Label(
    root,
    text="Movie Recommendation System",
    font=("Arial", 18, "bold"),
    bg="black",
    fg="white"  # Text color
)
heading.pack(pady=10)

# Input section
frame = tk.Frame(root, bg="black")  # Set background to black
frame.pack(pady=20)

movie_label = tk.Label(
    frame,
    text="Enter Movie Name: ",
    font=("Arial", 12),
    bg="black",
    fg="white"
)
movie_label.grid(row=0, column=0, padx=5)

entry = tk.Entry(
    frame,
    width=30,
    font=("Arial", 12),
    bg="black",
    fg="white",
    insertbackground="white"  # Cursor color
)
entry.grid(row=0, column=1, padx=5)

recommend_button = tk.Button(
    frame,
    text="Recommend",
    command=recommend_movie,
    font=("Arial", 12),
    bg="blue",
    fg="white"
)
recommend_button.grid(row=0, column=2, padx=5)

# Output section
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    justify="left",
    wraplength=400,
    bg="black",
    fg="white"
)
result_label.pack(pady=20)

# Footer
footer = tk.Label(
    root,
    text="Powered by Machine Learning",
    font=("Arial", 10, "italic"),
    fg="gray",
    bg="black"
)
footer.pack(side="bottom", pady=10)

# Run the Tkinter event loop
root.mainloop()
