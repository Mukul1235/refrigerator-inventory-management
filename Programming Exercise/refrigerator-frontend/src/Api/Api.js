import axios from "axios";

const API = axios.create({ baseURL: "http://127.0.0.1:8000/api/" });

export const fetchProducts = () => API.get("products/");
export const insertProduct = (data) => API.post("products/", data);
export const consumeProduct = (id, data) => API.post(`products/consume/${id}/`);
export const fetchExpiryAlerts = () => API.get("products/expiry-alerts/");
export const fetchShoppingList = () => API.get("shopping-list/");
