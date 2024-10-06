import snowflake.connector



# Create a connection to Snowflake

ctx = snowflake.connector.connect(
    user='Sanchit20',
    password='20Sep199120@',
    account='hwauhjp-iqb15817',
    warehouse='COMPUTE_WH',
    database='Data_Quality',
    role = 'ACCOUNTADMIN',
    schema ='Quality'
)
'''
ctx = snowflake.connector.connect(
    user='$SNOWFLAKE_USER',
    password='$SNOWFLAKE_PASSWORD',
    account='$SNOWFLAKE_ACCOUNT',
    warehouse='$SNOWFLAKE_WAREHOUSE',
    database='$SNOWFLAKE_DATABASE',
    schema='$SNOWFLAKE_SCHEMA'
)
'''

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


