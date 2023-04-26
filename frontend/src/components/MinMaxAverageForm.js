import React, { useEffect, useState } from 'react';
import axios from 'axios';

function MinMaxAverageForm() {
  // Define state variables for currency code, n, result, and error
  const [currencyCode, setCurrencyCode] = useState('USD');
  const [n, setN] = useState(5);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  // Fetch data from API when currencyCode or n changes
  useEffect(() => {
    async function fetchData() {
      // If currencyCode or n is not defined, clear result and error and return
      if (!currencyCode || !n) {
        setResult(null);
        setError(null);
        return;
      }

      try {
        // Define API url and send GET request using axios
        const url = `http://localhost:8000/api/min_max_average/${currencyCode}/${n}/`;
        const response = await axios.get(url);
        const data = response.data;

        // Extract data from response and set result and error state variables accordingly
        const maxDate = data.max_average_dates;
        const maxDiff = data.max_average;
        const minDate = data.min_average_dates;
        const minDiff = data.min_average;

        setResult(`For ${currencyCode} currency, the maximum average value was on ${maxDate}, at ${maxDiff.toFixed(4)}, while for the average value was on ${minDate}, at ${minDiff.toFixed(4)}.`);

        /*
        setResult({
          currency: data.currency,
          n: data.n,
          max_average: data.max_average.toFixed(4),
          min_average: data.min_average.toFixed(4),
          max_average_dates: data.max_average_dates,
          min_average_dates: data.min_average_dates,
        });
        */

        setError(null);
      } catch (error) {
        setResult(null);
        setError('Error retrieving data from API.');
      }
    }

    fetchData();
  }, [currencyCode, n]);

  // Handle changes in currency code input
  const handleCurrencyCodeChange = (event) => {
    setCurrencyCode(event.target.value);
  };

  // Handle changes in n input
  const handleNChange = (event) => {
    setN(event.target.value);
  };

  // Render the component
  return (
    <div className="container">
      <h2 className="mb-3">Max/Min Average Value</h2>
      <form className="row g-3">
        <div className="col-md-6">
          <label htmlFor="currency-code-input" className="form-label">
            Currency Code:
          </label>
          <input
            type="text"
            id="currency-code-input"
            className="form-control"
            value={currencyCode}
            onChange={handleCurrencyCodeChange}
          />
        </div>
        <div className="col-md-6">
          <label htmlFor="n-input" className="form-label">
            Last N Quotations:
          </label>
          <input
            type="number"
            id="n-input"
            className="form-control"
            value={n}
            onChange={handleNChange}
          />
        </div>
      </form>
      {/* Display error message if error state variable is not null */}
      {error && <p className="text-danger mt-3">{error}</p>}
      {/* Display result if result state variable is not null */}
      {result && <p className="mt-3">{result}</p>}
    </div>
  );
}

export default MinMaxAverageForm;
