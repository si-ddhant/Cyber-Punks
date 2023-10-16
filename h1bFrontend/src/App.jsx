import { useState } from "react";
import "./App.css";

import { Link } from "react-router-dom";
import { Route } from "react-router-dom";
import { BrowserRouter as Router, Routes } from "react-router-dom";

import RecordCount from "./RecordCount";
import MeanSalary from "./MeanSalary";
import MedianSalary from "./MedianSalary";

function App() {
  const routes = [
    { path: "/RecordCount", component: RecordCount, label: "Record Count" },
    { path: "/MeanSalary", component: MeanSalary, label: "Mean Salary" },
    { path: "/MedianSalary", component: MedianSalary, label: "Median Salary" },
  ];

  return (
    <Router>
      <div className="App">
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            {routes.map((route) => (
              <li key={route.path}>
                <Link to={route.path}>{route.label}</Link>
              </li>
            ))}
          </ul>
        </nav>

        <Routes>
          {routes.map((route) => (
            <Route
              key={route.path}
              path={route.path}
              element={<route.component />}
            />
          ))}
          <Route path="/api" element={<h2>Home</h2>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
