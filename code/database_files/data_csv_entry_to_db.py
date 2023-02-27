import mysql.connector
import pandas as pd

# Replace with your own database details
DATABASE_URL = "mysql://admin:forcapstone@solar-generation1.cdendtafbvez.us-east-2.rds.amazonaws.com:3306/solar-generation"

# Create a connection object
cnx = mysql.connector.connect(host='solar-generation1.cdendtafbvez.us-east-2.rds.amazonaws.com', user='admin', password='forcapstone', database='solar-generation')

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('../../data/raw/Solar_Energy_Generation.csv')

# Insert the DataFrame into the MySQL database
df.to_sql(name='my_table', con=cnx, if_exists='append', index=False)

# Close the database connection
cnx.close()