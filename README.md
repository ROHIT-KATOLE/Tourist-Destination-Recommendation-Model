# Tourist Destination Recommendation System
This project aims to recommend tourist destinations based on user input of location and category using machine learning techniques.

##  Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [API Endpoint](#api-endpoint)
- [Screenshots](#screenshots)
- [Contributing](#contributing)


## Features

- Recommend tourist places based on user-selected location and category.
- Uses Nearest Neighbors algorithm for recommendation.
- Provides a responsive web interface for easy interaction.

## Technologies Used
- Python
- Flask
- Pandas
- scikit-learn (sklearn)
- HTML/CSS/JavaScript
- jQuery

## Setup Instructions
1. Clone the repository:
```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

2. Set up virtual environment (optional but recommended):
```plaintext 
python -m venv venv
. venv/bin/activate  (for macOS/Linux)
. venv\Scripts\activate  (for Windows)
```

3. Run the Flask app:
```plaintext
python app.py
```
The app will run locally at http://localhost:5000.

## Usage
- Navigate to `http://localhost:5000` in your web browser.
- Select a location and category from the dropdown menus and click "Search".
- View recommended tourist places based on your selection.

## API Endpoint
- The recommendation API endpoint is accessible at `http://localhost:5000/recommend`.
- It accepts POST requests with JSON data containing `location` and `category` fields.

## Screenshots
- Include screenshots of your web application to give users a visual overview.

## Contributing
- Contributions are welcome! Please fork the repository and create a pull request.
