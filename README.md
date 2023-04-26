# NBP API

This project is designed to display information obtained from an external API endpoint in JSON format. The project is built with Django and utilizes the requests library for making API calls and parsing the JSON response. The project also incorporates a React front-end for displaying the data in a user-friendly manner.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python 3 installed on your local machine or development server.
- Django 3.x installed globally or in a virtual environment.
- Node.js and npm installed on your local machine or development server.
- React.js installed globally or in the project directory using npm.
- An understanding of HTML, CSS, JavaScript, and React.js.
- A code editor such as VS Code, Sublime Text, or Atom.

### Installing

--> 1. Clone the project to your local machine

```
  git clone https://github.com/alicjaz/nbp_api.git
```
--> 2. Move into the directory:
```
cd nbp_api
```

--> 3. Install the required Python packages using pip:
```
pip install -r requirements.txt
```

--> 4. Run the Django development server:
```
python manage.py runserver
```
--> 5. Deploy the server  
```
http://localhost:8000/
```
### Endpoints
- `/api/avg_exchange_rate/{currency_code}/{date}/` : This endpoint accepts two parameters: currency_code and date. It returns the average exchange rate of the specified currency on the specified date. The response is in JSON format.  

- `/api/min_max_average/{currency_code}/{n}/` : This endpoint accepts two parameters: currency_code and n. It returns the max and min average value of the specified currency for the last n days. The response is in JSON format.  

- `/api/buy_sell_difference/{currency_code}/{n}/` : This endpoint accepts two parameters: currency_code and n. It returns the difference between the buy and sell exchange rates of the specified currency for the last n days. The response is in JSON format.  


### Queries examples
- To query operation 1, run this command (which should have the value 5.2768 as the returning information):  
```
curl http://localhost:8000/api/avg_exchange_rate/GBP/2023-01-02/
```

- To query operation 2, run this command (which should have the values {"currency": "USD", "n": 2, "min_average": 4.1557, "min_average_dates": "2023-04-26", "max_average": 4.1649, "max_average_dates": "2023-04-25"}  as the returning information):  
```
curl http://localhost:8000/api/min_max_average/USD/2/
```

- To query operation 3, run this command (which should have the values {"max_difference_date": "2023-04-25", "max_difference": 0.08340000000000014, "min_difference_date": "2023-04-25", "min_difference": 0.08340000000000014}  as the returning information):  
```
curl http://localhost:8000/api/buy_sell_buy_sell_difference/USD/2/
```


### Built With
[Django](https://www.djangoproject.com/) - The web framework used  

[React](https://react.dev/) -  JavaScript library for building user interfaces  

[Django REST framework](https://www.django-rest-framework.org/) - Toolkit for building APIs  

### Author
Alicja Zalewska - [github](https://github.com/alicjaz)

## Screenshots
![Average Exchange Rate](https://i.ibb.co/XyC955C/avgexchangerate-View.png)

![Min Max Average](https://i.ibb.co/tCHqCGS/getmaxmin-Avg-View.png)

![Buy Sell Difference](https://i.ibb.co/ZhLGTYJ/buyselldiff-View.png)