import React from 'react';
import { BrowserRouter as Router, Link, Route, Routes } from 'react-router-dom'; // importing necessary components from 'react-router-dom' library
import AverageExchangeRateForm from './components/AverageExchangeRateForm'; // importing the form component for average exchange rate
import 'bootstrap/dist/css/bootstrap.min.css'; // importing Bootstrap CSS library

function App() {
  return (
    <Router> {/* Router component is used to manage the navigation state */}
      <div className="container">
        <h1 className="my-4">Welcome to Exchange Rates App!</h1>
        <nav className="mb-4">
          <ul className="nav">
            {/* Navigation links to various forms */}
            <li className="nav-item">
              <Link to="/" className="nav-link">Home</Link>
            </li>
            <li className="nav-item">
              <Link to="/avg_exchange_rate_form" className="nav-link">Average Exchange Rate</Link>
            </li>
          </ul>
        </nav>

        <Routes> {/* Routes component is used to define the routing */}
          <Route path="/" element={<div>Home</div>} /> {/* The default home route */}
          <Route path="/avg_exchange_rate_form" element={<AverageExchangeRateForm />} /> {/* The route for the average exchange rate form */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
