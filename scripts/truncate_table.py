import mysql.connector
import os
from dotenv import load_dotenv
from mysql.connector import Error

# Load environment variables from .env file
load_dotenv()

def delete_table_data(database_name, table_names, user, password, host='localhost'):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database_name
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Iterate over each table and delete its data
            for table_name in table_names:
                try:
                    # Delete all data from the table
                    truncate_query = f"TRUNCATE TABLE {table_name};"
                    cursor.execute(truncate_query)
                    print(f"Data from table `{table_name}` has been deleted and auto-increment value reset.")
                except Error as e:
                    print(f"Error truncating table `{table_name}`: {e}")

            # Commit the changes
            connection.commit()

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    # Database configuration from environment variables
    db_name = os.getenv("NAME")
    db_user = os.getenv("USER")
    db_password = os.getenv("PASSWORD")
    
    table_names = [
        'app_adviser',
        'app_boardmember',
        'app_documentationassistant',
        'app_documentationteam',
        'app_documentationteam_assistants',
        'app_esportsassistant', 
        'app_esportsteam',
        'app_esportsteam_assistants',
        'app_executivebanner',
        'app_executiveofficer',
        'app_highlightsevent',
        'app_marketingteam',
        'app_marketingteam_assistants',
        'app_marketingteamassistant',
        'app_multimediaassistant',
        'app_multimediateam',
        'app_multimediateam_assistants',
        'app_officeryear',
        'app_programmingassistant',
        'app_programmingteam',
        'app_programmingteam_assistants',
        'app_socialmediaassistant',
        'app_socialmediateam',
        'app_socialmediateam_assistants',
    ]
    
    delete_table_data(db_name, table_names, db_user, db_password)


# | Tables_in_icpep_data             |
# +----------------------------------+
# | app_aboutpic                     |
# | app_aboutuscontext               |
# | app_adviser                      |
# | app_banner                       |
# | app_boardmember                  |
# | app_documentationassistant       |
# | app_documentationteam            |
# | app_documentationteam_assistants |
# | app_esportsassistant             |
# | app_esportsteam                  |
# | app_esportsteam_assistants       |
# | app_executivebanner              |
# | app_executiveofficer             |
# | app_highlightsevent              |
# | app_marketingteam                |
# | app_marketingteam_assistants     |
# | app_marketingteamassistant       |
# | app_multimediaassistant          |
# | app_multimediateam               |
# | app_multimediateam_assistants    |
# | app_officeryear                  |
# | app_payment                      |
# | app_programmingassistant         |
# | app_programmingteam              |
# | app_programmingteam_assistants   |
# | app_socialmediaassistant         |
# | app_socialmediateam              |
# | app_socialmediateam_assistants   |
# | app_softwaretools                |
# | app_softwaretoolsresource        |
# | app_user                         |
