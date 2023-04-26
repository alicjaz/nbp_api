import React, { useEffect, useState } from 'react';

function BuySellForm() {
    // State variables to store currency code, n, difference, and error
    const [currencyCode, setCurrencyCode] = useState('USD');
    const [n, setN] = useState('5');
    const [difference, setDifference] = useState(null);
    const [error, setError] = useState(null);

    // Fetch data from API when currencyCode or n changes
    useEffect(() => {
        async function fetchData() {
            // If currencyCode or n is not set, reset the difference and error state variables
            if (!currencyCode || !n) {
                setDifference(null);
                setError(null);
                return;
            }

            // Otherwise, make a GET request to the API to retrieve buy/sell difference data
            const url = `http://localhost:8000/api/buy_sell_difference/${currencyCode}/${n}/`;
            const response = await fetch(url);

            // If the request is successful, set the difference state variable to the retrieved data
            if (response.status === 200) {
                const data = await response.json();
                const maxDate = data.max_difference_date;
                const maxDiff = data.max_difference;
                const minDate = data.min_difference_date;
                const minDiff = data.min_difference;

                setDifference(`For ${currencyCode} currency, the maximum exchange 
        difference was on ${maxDate}, at ${maxDiff.toFixed(4)}, while
        for the minimum exchange difference was on ${minDate}, at ${minDiff.toFixed(4)}.`);
                setError(null);
            }
            // Otherwise, reset the difference state variable and set the error state variable
            else {
                setDifference(null);
                setError('Error retrieving data from NBP API.');
            }
        }

        fetchData();
    }, [currencyCode, n]);

    // Render the form and the retrieved data if it exists
    return (
        <div className="container">
            <h2 className="mb-3">Buy Sell Difference</h2>
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
                    <label htmlFor="date-input" className="form-label">Last N Quotations:</label>
                    <input
                        type="text"
                        id="date-input"
                        className="form-control"
                        value={n}
                        onChange={(event) => setN(event.target.value)}
                    />
                </div>
            </form>
            {/* If there is an error, display it */}
            {error && (
                <p className="text-danger mt-3">{error}</p>
            )}
            {/* If there is difference data, display it */}
            {difference && (
                <p className="mt-3">
                    {difference}
                </p>
            )}
        </div>
    );
}

export default BuySellForm;
