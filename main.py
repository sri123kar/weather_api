from flask import Flask, jsonify
import mysql.connector
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)


#swagger Configs
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config = {
    'app_name': 'Weather App API'
    }
)
app.register_blueprint(SWAGGER_BLUEPRINT,url_prefix = SWAGGER_URL)
 # Connect to the MySQL database


def Conversion(n):
    return(n - 32.0) * 5.0 / 9.0


@app.route('/api/weather/<string:stationcode>/<string:date>', methods=['GET'])
def get_weather_data(stationcode,date):
    """
    Get all users
    ---
    responses:
      200:
        description: A list of users
    """
    # Execute a query to get all users
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="toor",
        database="weatherdataapp") 

    cursor = conn.cursor()
    query = "select * from weather WHERE StationCode = '"+ stationcode+"' AND Date(DT) = '"+ date+"'";
    cursor.execute(query)
    rows = cursor.fetchall()

    # Convert the rows to a list of dictionaries
    users = []
    for row in rows:
        user = {
            stationcode:{
            date:{
            "Maximum Temp": row[3],
            "Minimum Temp ": row[4],
            "precipitation": row[5]
            }
            }
        }
        users.append(user)

    # Close the database connection
    cursor.close()
    conn.close()
    

    # Return the users as a JSON response
    return jsonify(users)





@app.route('/api/weather/stats/<string:stationcode>/<string:year>', methods=['GET'])
def get_stats(stationcode,year):
    # Execute a query to get all users
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="toor",
        database="weatherdataapp") 

    cursor = conn.cursor()
    query = "select AverageMaxTemp,AverageMinTemp,Totalprecipitation from weatherstat where StationCode = '"+stationcode+"' and year = "+ year;
    cursor.execute(query)
    row = cursor.fetchone()

    # Convert the rows to a list of dictionaries
    data = {
        stationcode:{
        year:{
            "Maximum Avegrage temp in C": Conversion(row[0]),
            "Minimum Average temp in C": Conversion(row[1]),
            "precipitation in cm": row[2]/100
        }
        }
    }

    # Close the database connection
    cursor.close()
    conn.close()
    

    # Return the users as a JSON response
    return jsonify(data)




if __name__ == '__main__':
    app.run(debug=True)
    
