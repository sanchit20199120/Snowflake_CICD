import snowflake.connector
import os
# Create a connection to Snowflake

ctx = snowflake.connector.connect(
    user=os.getenv('SNOWFLAKE_USER'),
    password=os.getenv('SNOWFLAKE_PASSWORD'),
    account=os.getenv('SNOWFLAKE_ACCOUNT'),
    warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
    database=os.getenv('SNOWFLAKE_DATABASE'),
    schema=os.getenv('SNOWFLAKE_SCHEMA')
)

print("snowflake connection successfull")

# Create a cursor
cs = ctx.cursor()

# Run your SQL scripts here
try:
    with open('snowflake_code/V1.1.1__script.sql', 'r') as file:
        sql_script = file.read()
    cs.execute(sql_script)
finally:
    cs.close()
    ctx.close()


