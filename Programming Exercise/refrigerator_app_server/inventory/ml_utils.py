import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from .models import Product, PurchaseHistory, ConsumptionHistory

def generate_shopping_list():
    # Load historical data
    purchases = PurchaseHistory.objects.all()
    consumptions = ConsumptionHistory.objects.all()

    # Prepare the data
    data = []
    for purchase in purchases:
        consumption = consumptions.filter(product=purchase.product).first()
        data.append({
            'product': purchase.product.name,
            'quantity_purchased': purchase.quantity,
            'quantity_consumed': consumption.quantity if consumption else 0,
            'category': purchase.product.category
        })

    # Create a DataFrame
    df = pd.DataFrame(data)
    if df.empty:
        return {"message": "No data available for predictions"}

    # Encode categories (if category exists)
    if 'category' in df.columns and not df['category'].isnull().all():
        df['category'] = df['category'].astype('category').cat.codes
    else:
        df['category'] = 0  # Default to 0 if no categories

    # Define features and labels
    X = df[['quantity_consumed', 'category']]
    y = df['quantity_purchased']

    # Train the model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Generate predictions for the shopping list
    predictions = model.predict(X)

    # Create the shopping list
    shopping_list = []
    for i, pred in enumerate(predictions):
        shopping_list.append({
            'product': df.iloc[i]['product'],
            'predicted_quantity': round(pred, 2),
        })
    print(shopping_list)

    return shopping_list