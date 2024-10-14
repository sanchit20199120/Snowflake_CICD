import datetime
import pandas as pd
import snowflake.connector
from connector import aws_secret
from connector import connection
import sys

def file_ingestion(arg):
    args = arg[1].split(',')
    env = args[0]
# Connect to Snowflake
    try:
        dsn_meta, input_table, output_table, result_table, schema, database = connection.conn(env)

        log_dsn_name = aws_secret.get_dsn(dsn_meta)
        print(log_dsn_name)
        print(schema)
        print(database)

        # snowflake connection
        conn = snowflake.connector.connect(user=log_dsn_name['id'], password=log_dsn_name['secret'],
                                           account=log_dsn_name['host'], warehouse='COMPUTE_WH', schema=schema,
                                           database=database)

        print("Snowflake Successfully connected!!")
    except BaseException as e:
        print(e)


    # Read the CSV file
    file_path = 'file:/Users/sanchitbhardwaj/PycharmProjects/Snowflake_CICD/Data/TESTING_AUTOMATION_INPUT.csv'
    df = pd.read_csv(file_path)

    # Run Sequence to get the new job ID
    insert_run_job_seq = pd.read_sql_query("SELECT " + database + "." + schema + ".TESTING_AUTOMATION_INSERT_JOB_SEQ.nextval",conn)
    insert_run_job_id = str(insert_run_job_seq.iloc[0,0])

    # current timestamp
    date_time = datetime.datetime.now()

    # Adding two new column two DF
    df['JOB_ID'] = insert_run_job_id
    df['ISRT_DT_TM'] = date_time

    # Function to add single quote to df values
    def single_quote(val):
        if val == '':
            return 'NULL'
        return "'" + str(val).replace("'", "''") + "'"

    # adding single quote
    df = df.applymap(single_quote)


    # Insert data into Snowflake input table
    for index, row in df.iterrows():
        sql_query = "INSERT INTO " + input_table + " (JOB_ID,ISRT_DT_TM, WORKSTREAM_NAME, DATA_SRC_NAME, ADO_TESTCASE_NO\
        , TEST_STEP,TESTCASE_DESC, SOURCE_QUERY, TARGET_QUERY, EXPECTED_RESULT, IS_ACTIVE, IS_AUTOMATION_ENABLED, TEST_SUITES\
        , COMMENT,INSERTED_BY) VALUES"

        insert_query = sql_query + "(" + str(
            row['JOB_ID']) + "," + str(row['ISRT_DT_TM']) + "," + str(
            row['WORKSTREAM_NAME']) + "," + str(row['DATA_SRC_NAME']) + "," + str(
            row['ADO_TESTCASE_NO']) + "," + str(row['TEST_STEP']) + "," + str(
            row['TESTCASE_DESC']) + "," + str(row['SOURCE_QUERY']) + "," + str(
            row['TARGET_QUERY']) + "," + str(row['EXPECTED_RESULT']) + "," + str(
            row['IS_ACTIVE']) + "," + str(row['IS_AUTOMATION_ENABLED']) + "," + str(
            row['TEST_SUITES']) + "," + str(row['COMMENT']) + "," + str(
            row['INSERTED_BY']) + "),"

        print(insert_query)

        try:
            pd.read_sql_query(insert_query[:-1], conn)

        except BaseException as e:
            print(e)
        print("SUCCESS")


    # Close the connection
    conn.close()

file_ingestion(sys.argv)
