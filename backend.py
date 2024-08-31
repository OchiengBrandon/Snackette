import mysql.connector
import settings
import settings

# Connecting to a database

def connection_initialiser():
    try: 
        connection= mysql.connector.connect(
            user=settings.mysq_user,
            host='localhost',
            password = settings.msql_password
    )
        print(f"Connection in the server {connection} created succesfully")
    
    except:
        print("Connection Failed")
    finally:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS Snackette")
# Run
# connection_initialiser()

# Method For Creating connection
def createConnection(password):
    db_connection = mysql.connector.connect(
        user=settings.mysq_user,
        host='localhost',
        password = password,
        database='Snackette'
        )
    print("Connection Succesfully Created")
    return db_connection

def table_creation():
    connection = createConnection(settings.msql_password)
    my_cursor = connection.cursor()

    category_table_Query = """CREATE TABLE IF NOT EXISTS categories(
        category_id VARCHAR(6) NOT NULL,
        category_name VARCHAR(255) NOT NULL,
        description VARCHAR(255),
        PRIMARY KEY (category_id)
        )"""

    products_table_Query = """CREATE TABLE IF NOT EXISTS products(
        product_id VARCHAR(6) NOT NULL,
        name VARCHAR(255) NOT NULL,
        description VARCHAR(255),
        nutrients VARCHAR(255),
        category_id VARCHAR(255) NOT NULL,
        stockAmount INT NOT NULL,
        unitPrice DECIMAL(10, 2) NOT NULL,
        PRIMARY KEY (product_id),
        FOREIGN KEY (category_id) REFERENCES categories(category_id)
        )"""
        

    stock_table_query = """CREATE stock IF NOT EXISTS `stock` (
        stockId INT NOT NULL AUTO_INCREMENT,
        product_code VARCHAR(6) NOT NULL,
        unit_of_measurement VARCHAR(20) NOT NULL,
        stockAmount INT NOT NULL,
        DATETIME DEFAULT CURRENT_TIMESTAMP,
        recepientAccount INT NOT NULL,
        PRIMARY KEY (stockId),
        FOREIGN KEY (product_code) REFERENCES products(id_number)
    )"""


    # Creating Tables
    my_cursor.execute(category_table_Query)
    my_cursor.execute(products_table_Query)



    # Committing
    connection.commit()
    print("Updated...")

# Creating Tables
# table_creation()