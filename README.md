# 🎬 Movie Recommendation System

A simple and interactive **Movie Recommendation System** built using **Python and Streamlit**.  
This application recommends movies similar to the one selected by the user using a **content-based filtering approach**.

---

# 📌 Overview

Finding a good movie to watch can be difficult with thousands of options available.  
This project solves that problem by recommending movies similar to the one you like.

The system analyzes movie features such as **genres, keywords, cast, and crew**, and calculates similarity between movies to generate recommendations. Content-based recommendation systems compare movie attributes to suggest similar titles. :contentReference[oaicite:1]{index=1}

---

# 🚀 Features

- 🎥 Recommend movies based on user selection  
- 🖼️ Display movie posters  
- ⚡ Fast recommendation generation using similarity matrix  
- 💻 Interactive web interface using Streamlit  
- 📊 Data processing with Pandas and NumPy  

---

# 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **TMDB API**

---

# 📂 Project Structure

```
movie-recommendation-system/
│
├── app.py                  # Streamlit web application
├── movie_list.pkl          # Movie dataset
├── similarity.pkl          # Similarity matrix
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

---

# ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/GajjalaSandhya/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

### 3️⃣ Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run the application

```bash
streamlit run app.py
```

---

# 🌐 Usage

1. Open the application in your browser.
2. Select a movie from the dropdown list.
3. Click the **Recommend** button.
4. The system will display similar movie recommendations with posters.

---

# 🧠 How It Works

1. The dataset contains movie metadata such as genres, cast, crew, and keywords.
2. The text features are combined into a single format.
3. A **vectorization technique** is applied to convert text into numerical vectors.
4. **Cosine similarity** is calculated between movies.
5. The system recommends the most similar movies based on similarity scores.

---

# 📸 Demo

Example output:

- Selected Movie → **Avatar**
- Recommended Movies → Similar sci-fi and adventure movies.

---

# 🚀 Deployment

This project can be deployed on platforms like:

- Render
- Heroku
- Streamlit Cloud

---

# 📌 Future Improvements

- Add user login system  
- Add collaborative filtering  
- Improve recommendation accuracy  
- Add movie ratings and reviews  

---

# 👩‍💻 Author

**Sandhya Gajjala**

GitHub:  
https://github.com/GajjalaSandhya

---

# ⭐ Support

If you like this project, please **give it a star ⭐ on GitHub**.
