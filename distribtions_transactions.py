import psycopg2
import json

def lambda_handler(event, context):
    # Replace these with your PostgreSQL database connection details
    db_host = "your-db-host"
    db_name = "your-db-name"
    db_user = "your-db-user"
    db_password = "your-db-password"

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )

    try:
        # Create a cursor object to execute SQL queries
        with conn.cursor() as cursor:
            # Replace this query with your SELECT query
            select_query = "SELECT * FROM your_table"
            
            # Execute the SELECT query
            cursor.execute(select_query)

            # Fetch all rows from the result set
            rows = cursor.fetchall()

            # Convert the result to a list of dictionaries
            result = []
            for row in rows:
                result.append(dict(zip([column[0] for column in cursor.description], row)))

            # Print the result (for demonstration purposes)
            print(result)

            # You can further process or return the result as needed
            return {
                'statusCode': 200,
                'body': json.dumps(result)
            }

    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal Server Error'})
        }

    finally:
        # Close the database connection
        conn.close()

# Uncomment the line below for local testing
# lambda_handler({}, {})
