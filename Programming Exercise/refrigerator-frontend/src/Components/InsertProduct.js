import React, { useState } from "react";
import { insertProduct } from "../Api/Api";
import "../styles/InsertProduct.css";

function InsertProduct() {
  const [product, setProduct] = useState({
    name: "",
    quantity: "",
    unit: "",
    expiration_date: "",
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await insertProduct(product);
      alert("Product added successfully!");
      setProduct({ name: "", quantity: "", unit: "", expiration_date: "" });
    } catch (error) {
      console.error(error);
      alert("Error adding product");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Product Name"
        value={product.name}
        onChange={(e) => setProduct({ ...product, name: e.target.value })}
      />
      <input
        type="number"
        placeholder="Quantity"
        value={product.quantity}
        onChange={(e) => setProduct({ ...product, quantity: e.target.value })}
      />
      <select
        value={product.unit}
        onChange={(e) => setProduct({ ...product, unit: e.target.value })}
      >
        <option value="">Select Unit</option>
        <option value="litre">Liter</option>
        <option value="gram">Gram</option>
      </select>
      <input
        type="date"
        value={product.expiration_date}
        onChange={(e) =>
          setProduct({ ...product, expiration_date: e.target.value })
        }
      />
      <button type="submit">Add Product</button>
    </form>
  );
}

export default InsertProduct;