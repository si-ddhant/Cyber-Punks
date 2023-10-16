// RecordCount.js
import React, { useState, useEffect } from "react";
import axios from "axios";

function RecordCount() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    axios.get("http://localhost:8000/api/record-count/").then((response) => {
      setCount(response.data.count);
    });
  }, []);

  return (
    <div>
      <h2>Record Count</h2>
      <p>Total Number of Records: {count}</p>
    </div>
  );
}

export default RecordCount;
