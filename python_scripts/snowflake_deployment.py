import snowflake.connector
import os
import glob
# Create a connection to Snowflake

ctx = snowflake.connector.connect(
    user=os.getenv('SNOWFLAKE_USER'),
    password=os.getenv('SNOWFLAKE_PASSWORD'),
    account=os.getenv('SNOWFLAKE_ACCOUNT'),
    warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
    database=os.getenv('SNOWFLAKE_DATABASE'),
    schema=os.getenv('SNOWFLAKE_SCHEMA')
)

print("Snowflake Connection Successful !!")

# Create a cursor
cs = ctx.cursor()

try:
    # Specify the directory to search for .sql files
    directory = "snowflake_code"

    # Use glob to find .sql files
    sql_files = glob.glob(f'{directory}/*.sql')

    if sql_files:  # Check if the list is not empty
        for filepath in sql_files:
            print(f'Found SQL file: {filepath}')

            # Run your SQL scripts here
            with open(filepath, 'r') as file:
                sql_script = file.read()
            cs.execute(sql_script)
            print("Deployment Successful!!")
    else:
        print('No files found with ending .sql')

finally:
    cs.close()
    ctx.close()


