# FoodSales
To Run the peoject
1.create virtualenv
2.pip install -r requirements.txt
3.py manage.py makemigrations
4.py manage.py migrate
5.py manage.py runserver

To test apis:
1.To upload files:POST http://127.0.0.1:8000/
2.To get data by product name:GET http://127.0.0.1:8000/Food
2. To get data by product name limit 5:POST http://127.0.0.1:8000/Food
