# WEATHER_API
API to fetch weather data


### STEP 1 -> Creating the database 

*Create a database in your local mysql is recommended.

*After installing and setting up the database make sure to note down username,password and hostname which we will use in next step.

*Run DDL Commands in order it is given in 'DDL Commands' File.


### STEP 2 -> Reading the data from text file and store in the databse

*Open the Jupitar notebook in your local.

*Run given command for installing the required packages.

   *command 1 -> !pip install mysql-connector-python.

*Give file location for example if you files present in C:\Users\kv823\txttodatabse then we can enter C:/Users/kv823/txttodatabse
and make sure that all the text files and python notebook present in same location(project sepecific we can make it from any location from code)
make sure you entered the correct password 

*After uploading the files if we want to update the data of a station code then we can put that file in merg folder present in the same locaton and the run merg function 

*We have to create other function because every time some data got update then other table data get also affected 


### STEP 3 ->Run the api

*Install python in your system and make sure it is added in system variable

*Two files is needed to run the api first one is main.py and second one is static/swagger.json

*Then place these file in any location but put it in the together

*Open terminal in that location and run below commands one by one so that required package is installed
    command 1 -> pip install mysql-connector-python
    command 2 -> pip install flask
    command 3 -> pip install flask-swagger-ui
    command 4 -> python main.py

*After running 4th command our endpoint is live 

*Just copy the local host ip address along with the port no. then add the postfix '/swagger' in the url and hit enter

*The one swagger endpoint got opened which has two api endpoint we can input the data and get desired value 



> problem 1 -> DDL Commands.txt

> problem 2 -> data_ingestion and data_analysis.ipynb

> problem 3 -> data_ingestion and data_analysis.ipynb

> problem 4 -> main.py

> Deployment -> Extra Credit.txt



**Thankyou**


