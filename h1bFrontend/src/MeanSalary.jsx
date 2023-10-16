// MeanSalary.js
import React, { useState, useEffect } from "react";
import axios from "axios";

function MeanSalary() {
  const [meanSalary, setMeanSalary] = useState(1);

  useEffect(() => {
    axios.get("http://localhost:8000/api/mean-salary/").then((response) => {
      setMeanSalary(response);
      console.log(response);
    });
  }, []);

  return (
    <div>
      <h2>Mean Salary</h2>
      <p>Mean Salary: ${meanSalary}</p>
    </div>
  );
}

export default MeanSalary;
