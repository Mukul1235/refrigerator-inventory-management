import React, { useEffect, useState } from "react";
import { fetchShoppingList } from "../Api/Api";

function ShoppingList() {
  const [shoppingList, setShoppingList] = useState([]);

  useEffect(() => {
    const fetchList = async () => {
      const response = await fetchShoppingList();
      setShoppingList(response.data);
    };
    fetchList();
  }, []);

  return (
    <div>
      <h2>Shopping List</h2>
      {shoppingList.length > 0 ? (
        shoppingList.map((item, index) => (
          <p key={index}>
            {item.product}: {item.predicted_quantity}
          </p>
        ))
      ) : (
        <p>No shopping recommendations</p>
      )}
    </div>
  );
}

export default ShoppingList;
