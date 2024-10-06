import snowflake.connector

# Create a connection to Snowflake
ctx = snowflake.connector.connect(
    user='$SF_USER',
    password='$SF_PASSWORD',
    account='$SF_ACCOUNT',
    warehouse='$SF_WAREHOUSE',
    database='$SF_DATABASE',
    schema='$SF_SCHEMA'
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


