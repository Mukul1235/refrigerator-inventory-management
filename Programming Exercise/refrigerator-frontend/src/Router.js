
import React from "react";
import { Routes, Route } from "react-router-dom";
import Home from "./Pages/Home";
import ManageProducts from "./Pages/ManageProducts";
import Alerts from "./Pages/Alerts";

function AppRouter() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/manage-products" element={<ManageProducts />} />
      <Route path="/alerts" element={<Alerts />} />
    </Routes>
  );
}

export default AppRouter;