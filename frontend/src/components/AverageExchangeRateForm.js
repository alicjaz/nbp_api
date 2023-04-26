import React, {useEffect, useState} from 'react';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';

function AverageExchangeRateForm() {
    // Declare state variables for currency code, date, and average exchange rate
    const [currencyCode, setCurrencyCode] = useState("USD");
    const [date, setDate] = useState(new Date());
    const [averageExchangeRate, setAverageExchangeRate] = useState(null);

    // Fetch data from API when currency code or date changes
    useEffect(() => {
        async function fetchData() {
            // Construct API URL using currency code and date
            const url = `http://localhost:8000/api/avg_exchange_rate/${currencyCode}/${date.toISOString().slice(0, 10)}/`;
            // Fetch data from API
            const response = await fetch(url);
            // Parse response as JSON
            const data = await response.json();
            // Extract average exchange rate from data and update state
            const averageExchangeRate = data.average_exchange_rate;
            setAverageExchangeRate(averageExchangeRate);
        }

        fetchData();
    }, [currencyCode, date]);

    return (
        <div className="container">
            <h2 className="mb-3">Average Exchange Rate</h2>
            <form className="row g-3">
                <div className="col-md-6">
                    <label htmlFor="currency-code-input" className="form-label">Currency Code:</label>
                    <input
                        type="text"
                        id="currency-code-input"
                        className="form-control"
                        value={currencyCode}
                        onChange={(event) => setCurrencyCode(event.target.value)}
                    />
                </div>
                <div className="col-md-6">
                    <label htmlFor="date-input" className="form-label">Date:</label>
                    <DatePicker
                        id="date-input"
                        className="form-control"
                        selected={date}
                        onChange={(value) => setDate(value)}
                        dateFormat="yyyy-MM-dd"
                    />
                </div>
            </form>
            {/* Display average exchange rate if it has been fetched */}
            {averageExchangeRate && (
                <p className="mt-3">
                    As of {date.toISOString().slice(0, 10)} the average exchange rate
                    for {currencyCode} is {averageExchangeRate}.
                </p>
            )}
        </div>
    );
}

export default AverageExchangeRateForm;
