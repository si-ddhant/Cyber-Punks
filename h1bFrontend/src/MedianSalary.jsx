// MedianSalary.js
import React, { useState, useEffect } from "react";
import axios from "axios";

function MedianSalary() {
  const [medianSalary, setMedianSalary] = useState(0);

  useEffect(() => {
    // Replace with your custom API endpoint for calculating the median salary
    axios.get("http://localhost:8000/api/median-salary/").then((response) => {
      setMedianSalary(response.data.median_salary);
    });
  }, []);

  return (
    <div>
      <h2>Median Salary</h2>
      <p>Median Salary: ${medianSalary}</p>
    </div>
  );
}

export default MedianSalary;
