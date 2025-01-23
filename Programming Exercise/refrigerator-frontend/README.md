
# Refrigerator App

A full-stack application to manage products in a refrigerator. The app allows users to insert, consume, and monitor items, keep track of expiration dates, and generate shopping lists using machine learning.

---

## Features

### Stage 1: Basic Product Management
- **Insert Items**: Add products to the refrigerator with a quantity and unit.
- **Consume Items**: Update how much of a product is used (e.g., 250g vegetables or half a liter of milk).
- **Status Check**: Track the current quantity of each item.
- **History Log**: View a history of purchases and consumption.

### Stage 2: Expiration Management
- **Expiration Alerts**: Notify users of items nearing their expiration date.
- **Auto-Removal**: Automatically deduct expired items from the inventory and prompt the user to remove them.

### Stage 3: Smart Shopping List
- **Machine Learning Integration**: 
  - Analyze past shopping and consumption patterns.
  - Recommend items for the shopping list to prevent stockouts.

---

## Tech Stack

### Frontend:
- ReactJS (with React Router for navigation)
- TailwindCSS (for styling)

### Backend:
- Django (REST API framework)
- PostgreSQL (database)
- Django REST Framework (DRF) for API endpoints
- Django CORS Headers (to allow frontend-backend communication)

### Machine Learning:
- `scikit-learn` for analyzing consumption data and generating shopping lists.

---

## Installation Guide

### 1. Prerequisites
Ensure you have the following installed:
- **Node.js**: [Download Node.js](https://nodejs.org/)
- **Python 3.8+**: [Download Python](https://www.python.org/)

### 2. Clone the Repository
```bash
git clone <repository-url>
cd refrigerator-app
```

---

### 3. Setting Up the Backend

#### Install Python dependencies:
```bash
cd backend
pip install -r requirements.txt
```

#### Configure PostgreSQL:
1. Create a database:
   ```sql
   CREATE DATABASE refrigerator_app;
   ```
2. Create a user:
   ```sql
   CREATE USER refrigerator_user WITH PASSWORD 'your_password';
   ```
3. Grant privileges:
   ```sql
   GRANT ALL PRIVILEGES ON DATABASE refrigerator_app TO refrigerator_user;
   ```

#### Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

#### Start the backend server:
```bash
python manage.py runserver
```

---

### 4. Setting Up the Frontend

#### Install Node.js dependencies:
```bash
cd ../frontend
npm install
```

#### Start the frontend server:
```bash
npm start
```

---

### 5. Machine Learning Setup

1. Install ML dependencies:
   ```bash
   pip install pandas numpy scikit-learn
   ```

2. ML files are located in the `ml` directory. Ensure they are correctly linked to the backend.

---

## API Endpoints

| Endpoint                    | Method | Description                          |
|-----------------------------|--------|--------------------------------------|
| `/api/products/`            | GET    | Get all products in the refrigerator.|
| `/api/products/add/`        | POST   | Add a new product.                   |
| `/api/products/consume/`    | POST   | Consume a product.                   |
| `/api/products/expired/`    | GET    | Get a list of expired items.         |
| `/api/shopping-list/`       | GET    | Get ML-generated shopping suggestions.|

---

## Project Structure

```
refrigerator-app/
├── backend/
│   ├── api/                     # Django app with models and views
│   ├── ml/                      # ML scripts and logic
│   ├── manage.py                # Django management script
│   ├── requirements.txt         # Python dependencies
│   └── settings.py              # Backend configuration
├── frontend/
│   ├── src/
│   │   ├── components/          # Reusable React components
│   │   ├── pages/               # Page-level components
│   │   ├── App.js               # Main React app file
│   │   ├── index.js             # Entry point
│   │   └── styles/              # TailwindCSS configuration
│   ├── public/
│   └── package.json             # Node.js dependencies
└── README.md                    # Project documentation
```

---

## To-Do

1. Add unit tests for both frontend and backend.
2. Improve ML model for better predictions.
3. Deploy the app to the cloud.

---

## License

This project is licensed under the MIT License. 
