import React from "react";
import InsertProduct from "../Components/InsertProduct";
import ShoppingList from "../Components/ShoppingList";
import "../styles/ManageProducts.css"; 

function ManageProducts() {
  return (
    <div className="manage-products-container">
      <h1>Manage Products</h1>
      <InsertProduct />
      <ShoppingList />
    </div>
  );
}

export default ManageProducts;