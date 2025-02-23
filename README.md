# Project Title: Software Engineer's Salary Prediction

A machine learning web app built with Streamlit to predict software engineer salaries based on the Stack Overflow 2020 Developer Survey data, using a Decision Tree Regressor.

## Overview

This project leverages the rich dataset from Stack Overflow's 2020 Developer Survey to predict salaries for software engineers. The app is powered by a Decision Tree Regressor model and deployed using Streamlit, providing an interactive interface for users to explore predictions based on input features like years of experience, education level, and more.

## Features

- **Interactive UI**: Built with Streamlit for a seamless user experience.
- **Prediction Model**: Utilizes a Decision Tree Regressor to estimate salaries.
- **Dataset**: Sourced from Stack Overflow’s 2020 Developer Survey.
- **Custom Inputs**: Users can tweak parameters to see how predictions change.

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/anugrahrk/salary_predictor.git
   cd your-repo-name
2. **Install Dependencies**:
Ensure you have Python installed (preferably 3.8+). Then, install the required packages:
    ```bash

    pip install -r requirements.txt
3. **Run the App**:
Launch the Streamlit app with the following command:

   
        streamlit run app.py
This will start a local server, and you can access the app in your browser (typically at http://localhost:8501).
## Dependencies

- `streamlit`: For the web app interface.
- `scikit-learn`: For the Decision Tree Regressor model.
- `pandas`: For data manipulation.
- `numpy`: For numerical operations.

(Include these in a `requirements.txt` file for easy setup.)

## Dataset

The model is trained on the Stack Overflow 2020 Developer Survey dataset, which includes features like:

- Years of professional coding experience
- Education level
- Job role
- Country
- And more!

The dataset is preprocessed to handle missing values and categorical variables before feeding into the Decision Tree Regressor.

## Usage

1. Open the app in your browser after running `streamlit run app.py`.
2. Input relevant features (e.g., years of experience, education, country) via the sidebar or input fields.
3. View the predicted salary output based on the Decision Tree Regressor.

## Project Structure

```bash
  salary_predicto/
├── app.py              # Main Streamlit app file
├── survey_results_public_2020.csv     #  Dataset 
├── saved_steps.pkl     # Trained Decision Tree Regressor model
├── predict_page.py     # Prediction page
├── SWE Salary Prediction.ipynb        # Jupyter Notebook used for training the model
├── requirements.txt    # List of Python dependencies
└── README.md           # This file
