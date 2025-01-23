import React from "react";
import { BrowserRouter as Router } from "react-router-dom";
import AppRouter from "./Router";
import Header from "./Components/Header";

function App() {
  return (
    <Router>
      <Header />
      <AppRouter />
    </Router>
  );
}

export default App;