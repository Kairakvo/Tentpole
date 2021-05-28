# Tentpole technical interview

A simple django application that takes in customer details, together whith an excel file and renders a graph showing income and expenditure for the past 12 months.
## Assumptions
1. Have python3 installed, to be safe version 3.9.2
2. The excel file has only one sheet named "sheet1", which contains the month,income and expenditure.


## USAGE
1.Use a virtual envrironment-venv to run the application. Fisrst download all the code folder, open it and ececute the following commands in the cmd.(windows 10). 
    
    
    py -m venv venv
    venv\Sripts\activate
    pip install django
    
2. To run the application,excute:
    
    python manage.py runserver
    
3.Then go to the browser and open local address

    http://127.0.0.1:8000/
4. type in the required fiels, upload your file and then press submit
