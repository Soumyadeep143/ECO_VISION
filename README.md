# Economic Data Analysis & Prediction Dashboard

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-black?style=for-the-badge&logo=flask)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E?style=for-the-badge&logo=scikit-learn)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-yellow?style=for-the-badge&logo=javascript)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

An interactive web dashboard for analyzing and predicting economic indicators for various countries. This tool allows users to select economic parameters, choose a machine learning model, and visualize the results. It also leverages the Gemini API to provide AI-driven insights and suggestions based on the data.

## 📋 Features

*   **Country & Parameter Selection**: Choose from a list of countries and multiple economic indicators.
*   **Machine Learning Models**: Apply different regression models to predict trends:
    *   Decision Tree
    *   Random Forest
    *   Support Vector Machine (SVM)
    *   Polynomial Regression
*   **Dynamic Visualizations**: Render predictions using various chart types like Line, Bar, Scatter, and Area charts.
*   **AI-Powered Insights**: Generate qualitative analysis and suggestions using Google's Gemini AI.
*   **Model Performance Metrics**: View R², MAE (AAE), and RMSE (SE) for each model prediction to assess accuracy.
*   **Data Export**: Export raw data to CSV and export reports (including charts and AI summary) to PDF.

## 🛠️ Tech Stack

*   **Backend**:
    *   **Framework**: Flask
    *   **ML Libraries**: Scikit-learn, Pandas, NumPy
    *   **PDF/Image Generation**: ReportLab, Matplotlib
    *   **Environment**: `python-dotenv`

*   **Frontend**:
    *   **Languages**: Vanilla JavaScript (ES6+), HTML5, CSS3
    *   **Charting**: Chart.js
    *   **API Communication**: Fetch API

*   **External Services**:
    *   **Google Gemini API**: For generating AI-driven summaries.

## 📂 Project Structure

```
MP/
├── backend/
│   ├── datasets/
│   │   └── gdpdataset_cleaned.csv
│   ├── .env                   # Secret keys (ignored by Git)
│   ├── ml_backend.py          # Main Flask application
│   ├── CHECK_MODEL.PY         # Utility to check Gemini models
│   └── requirements.txt       # Backend dependencies
├── frontend/
│   ├── index.html             # Main HTML file
│   ├── script.js              # Frontend logic
│   └── styles.css             # Styling
└── .gitignore                 # Specifies files for Git to ignore
└── README.md                  # This file
```

## 🚀 Setup and Installation

Follow these steps to get the project running locally.

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd "MP"
```

### 2. Set Up the Backend

**a. Create a Virtual Environment:**

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**b. Install Dependencies:**

Create a `requirements.txt` file inside the `backend` folder with the following content:

```txt
# backend/requirements.txt
Flask
pandas
scikit-learn
matplotlib
numpy
python-dotenv
requests
reportlab
```

Then, install the packages:

```bash
pip install -r backend/requirements.txt
```

**c. Configure Environment Variables:**

Create a file named `.env` inside the `backend` directory and add your Gemini API key:

```env
# backend/.env
GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
```

### 3. Run the Application

Execute the main Flask script to start the server.

```bash
python backend/ml_backend.py
```

The application will be available at `http://127.0.0.1:5000`.

## 🌐 API Endpoints

The backend exposes the following RESTful endpoints:

| Method | Endpoint                  | Description                                                                 |
| :----- | :------------------------ | :-------------------------------------------------------------------------- |
| `GET`  | `/countries`              | Returns a sorted list of all available countries.                           |
| `POST` | `/predict`                | Runs a prediction model. Expects `country`, `parameters`, and `algorithm`.  |
| `POST` | `/gemini-summary`         | Proxies a prompt to the Gemini API and returns the AI-generated summary.    |
| `GET`  | `/export/csv`             | Exports filtered country data for selected parameters as a CSV file.        |
| `GET`  | `/export/png`             | Exports a chart for a single parameter as a PNG image.                      |
| `GET`  | `/export/pdf`             | Exports a full report with charts and AI summary as a PDF document.         |

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

*This README was generated to provide a clear and professional overview of the project.*