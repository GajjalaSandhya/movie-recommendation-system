# Movie Recommender System 🎬

A **Python-based web application** built with **Streamlit** that recommends movies similar to a selected movie and displays their posters. It uses a precomputed similarity matrix and TMDB API for fetching posters.  

---

## Features

- Select a movie from a dropdown list of popular movies.  
- Get **top 5 recommended movies** similar to the selected movie.  
- View movie posters for recommended movies.  
- Simple and interactive **Streamlit interface**.  
- Automatically downloads necessary data files from **Google Drive**.  

---

## Tech Stack

- **Python 3**  
- **Streamlit** for the web interface  
- **Pandas** for data handling  
- **Pickle** for loading precomputed datasets  
- **Requests** for fetching movie posters from TMDB API  
- **gdown** for downloading files from Google Drive  

---

## Project Structure

```text
Movie-Recommender-System/
│
├─ app.py                  # Main Streamlit app
├─ movie_dict.pkl          # Pickled movie dictionary
├─ movies.pkl              # Pickled movie DataFrame
├─ similarity.pkl          # Pickled similarity matrix
├─ requirements.txt        # Python dependencies
└─ README.md               # Project documentation

##Setup and installation

Clone the repository

git clone <your-repo-url>
cd Movie-Recommender-System

Create a virtual environment (optional but recommended)

python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

Install dependencies

pip install -r requirements.txt

Run the app

streamlit run app.py

Open your browser and visit the URL displayed in the terminal (usually http://localhost:8501).

Deployment on Render

Add your Python 3 runtime in runtime.txt (e.g., python-3.12).

Set the Start Command in Render as:

streamlit run app.py --server.port $PORT --server.address 0.0.0.0

Add all dependencies to requirements.txt.

Deploy the project; Render will automatically run the Start Command.

How It Works

Data Loading

Downloads three files from Google Drive if not already present:

movie_dict.pkl → movie dictionary

movies.pkl → pandas DataFrame of movies

similarity.pkl → precomputed similarity matrix

Recommendation Logic

When a movie is selected, the app finds its index in the DataFrame.

Retrieves similarity scores from the similarity matrix.

Returns top 5 movies sorted by similarity.

Poster Fetching

Uses TMDB API to fetch posters for recommended movies.

Streamlit Interface

Displays movie names and posters in 5 columns for easy viewing.

Requirements
streamlit
pandas
numpy
requests
gdown
pickle-mixin
Screenshots


Screenshot showing the dropdown selection and recommended movie posters.

Future Improvements

Add user ratings for personalized recommendations.

Include movie genres or release year filtering.

Deploy a faster caching system for TMDB API calls.

Make the app mobile-responsive.

License

This project is open source and available under the MIT License.


---

This version is **fully formatted** for GitHub and will look professional. ✅  

If you want, I can also make a **ready-to-paste `requirements.txt`** file that matches your app perfectly for deployment on Render, so you don’t get any missing module errors.  

Do you want me to do that next?
