import React, { useState } from "react";
import { consumeProduct } from "../Api/Api";

function ConsumeProduct({ productId }) {
  const [quantity, setQuantity] = useState("");

  const handleConsume = async () => {
    try {
      await consumeProduct(productId, { quantity });
      alert("Product consumed successfully!");
      setQuantity("");
    } catch (error) {
      console.error(error);
      alert("Error consuming product");
    }
  };

  return (
    <div>
      <input
        type="number"
        placeholder="Quantity to Consume"
        value={quantity}
        onChange={(e) => setQuantity(e.target.value)}
      />
      <button onClick={handleConsume}>Consume</button>
    </div>
  );
}

export default ConsumeProduct;
