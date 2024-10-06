CREATE OR REPLACE TABLE TESTING_AUTOMATION_INPUT(
JOB_ID VARCHAR,
ISRT_DT_TM TIMESTAMP_NTZ(9),
WORKSTREAM_NAME VARCHAR,
DATA_SRC_NAME VARCHAR,
ADO_TESTCASE_NO VARCHAR,
TEST_STEP VARCHAR,
TESTCASE_DESC VARCHAR,
SOURCE_QUERY VARCHAR,
TARGET_QUERY VARCHAR,
EXPECTED_RESULT VARCHAR,
IS_ACTIVE VARCHAR,
IS_AUTOMATION_ENABLED VARCHAR,
TEST_SUITES VARCHAR,
COMMENT VARCHAR,
INSERTED_BY VARCHAR
);