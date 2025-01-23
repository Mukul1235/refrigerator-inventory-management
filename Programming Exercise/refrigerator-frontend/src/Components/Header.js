import React from "react";
import { Link } from "react-router-dom";
import "../styles/Header.css"; 

function Header() {
  return (
    <nav>
      <h1>Refrigerator App</h1>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/manage-products">Manage Products</Link>
        </li>
        <li>
          <Link to="/alerts">Alerts</Link>
        </li>
      </ul>
    </nav>
  );
}

export default Header;