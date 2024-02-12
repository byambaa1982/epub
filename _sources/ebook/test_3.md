
# Test 1

## Question 1

Which of the following is a key feature of a data lakehouse that distinguishes it from traditional data warehouses?

- A. A data lakehouse relies solely on structured data.
- B. A data lakehouse supports schema enforcement and governance.
- C. A data lakehouse is limited to batch processing only.
- D. A data lakehouse requires separate storage and compute resources.
- E. A data lakehouse is optimized for OLTP workloads.

```{toggle}
Correct Answer: B. A data lakehouse supports schema enforcement and governance.

Exam Topic: Databricks Lakehouse Platform

Explanation: A data lakehouse combines the benefits of a data lake and a data warehouse. It supports schema enforcement and governance, which is a key feature that distinguishes it from traditional data warehouses. Unlike data lakes, which often lack governance, and data warehouses, which may not handle unstructured data well, lakehouses provide a unified platform for all types of data while maintaining governance and reliability.

```

## Question 2

In a Databricks environment, where are the data and compute resources located when processing data?

- A. In the user's local environment
- B. In the Databricks workspace
- C. In the cloud provider's data centers
- D. In the Databricks corporate servers
- E. In a hybrid cloud setup

```{toggle}
Correct Answer: C. In the cloud provider's data centers

Exam Topic: Databricks Lakehouse Platform

Explanation: In a Databricks environment, both the data and compute resources are located in the cloud provider's data centers. Databricks leverages cloud infrastructure to manage and process data, providing scalability and flexibility.

```

## Question 3

How can a data lakehouse facilitate the requirements of both real-time analytics and secure, governed batch processing?

- A. By providing a single, immutable copy of data for all workloads.
- B. By enforcing strict schema-on-read for all data types.
- C. By offering separate storage solutions for each workload type.
- D. By enabling fine-grained security and concurrent data processing.
- E. By relying exclusively on in-memory data processing.

```{toggle}
Correct Answer: D. By enabling fine-grained security and concurrent data processing.

Exam Topic: Databricks Lakehouse Platform

Explanation: A data lakehouse is designed to support various types of workloads, including real-time analytics and secure, governed batch processing. It enables fine-grained security controls and allows for concurrent data processing, which means that it can handle both unstructured data for analytics and structured data for batch processing with the necessary governance in place.

```

## Question 4

When should a data engineer opt for an Interactive cluster over a Job cluster in Databricks?

- A. When running scheduled batch jobs to process data at regular intervals.
- B. When performing exploratory data analysis in a collaborative environment.
- C. When executing a long-running ETL job that requires high reliability.
- D. When triggering a pipeline based on an event or a specific condition.
- E. When optimizing for cost and using spot instances for processing.

```{toggle}
Correct Answer: B. When performing exploratory data analysis in a collaborative environment.

Exam Topic: Production Pipelines

Explanation: Interactive clusters are best suited for exploratory data analysis, where collaboration and interactivity are key. They allow multiple users to work together and share insights in real-time. Job clusters, on the other hand, are optimized for running scheduled jobs and automated workflows.

```

## Question 5

What feature of the Databricks Lakehouse Platform should a data engineer use to manage access control for a Delta table?

- A. Repos
- B. Unity Catalog
- C. Workflows
- D. SQL Analytics
- E. MLflow

```{toggle}
Correct Answer: B. Unity Catalog

Exam Topic: Data Governance

Explanation: Unity Catalog in Databricks Lakehouse Platform is used to manage access control and governance across all data assets, including Delta tables. It allows data engineers to grant and revoke permissions, ensuring that only authorized users have access to specific data.

```

## Question 6

What feature of Databricks Notebooks enhances collaboration among data engineers and data scientists?

- A. The ability to execute notebooks as jobs
- B. The integration with Git for version control
- C. The support for multiple programming languages
- D. The real-time coauthoring capabilities
- E. The built-in data visualization tools

```{toggle}
Correct Answer: D. The real-time coauthoring capabilities

Exam Topic: ELT with Spark SQL and Python

Explanation: Databricks Notebooks support real-time coauthoring, allowing multiple users to edit the same notebook simultaneously. This feature enhances collaboration among team members, making it easier to work together on complex data engineering and data science tasks.

```

## Question 7

How do Databricks Repos support Continuous Integration/Continuous Deployment (CI/CD) in the Databricks Lakehouse Platform?

- A. By providing a built-in scheduler for job execution
- B. By enabling the use of webhooks to trigger workflows
- C. By allowing users to create and manage Git branches
- D. By automating the deployment of notebooks to production
- E. By integrating with external CI/CD tools for automated testing and deployment

```{toggle}
Correct Answer: E. By integrating with external CI/CD tools for automated testing and deployment

Exam Topic: Production Pipelines

Explanation: Databricks Repos integrate with external CI/CD tools, enabling automated testing and deployment of code changes. This integration helps streamline the development process, ensuring that new features and updates can be rolled out efficiently and reliably.

```

## Question 8

What is Delta Lake's primary role within the Databricks ecosystem?

- A. To provide a machine learning platform for model training and deployment.
- B. To serve as a high-performance query engine for big data analytics.
- C. To act as a transactional storage layer that brings reliability to data lakes.
- D. To offer a distributed computing framework for large-scale data processing.
- E. To function as a real-time streaming engine for event-driven applications.

```{toggle}
Correct Answer: C. To act as a transactional storage layer that brings reliability to data lakes.

Exam Topic: Incremental Data Processing

Explanation: Delta Lake is an open-source storage layer that brings ACID transactions, scalable metadata handling, and unifies streaming and batch data processing to data lakes. It provides reliability, governance, and performance to data stored in a data lake.

```

## Question 9

Which SQL DDL command correctly creates a new Delta table with the specified schema, replacing any existing table with the same name?

- A. 
```sql
CREATE TABLE IF NOT EXISTS new_table (
id INT,
birthDate DATE,
avgRating DOUBLE
) USING DELTA
```
- B. 
```sql
CREATE OR REPLACE TABLE new_table (
id INT,
birthDate DATE,
avgRating DOUBLE
) USING DELTA
```
- C. 
```sql
DROP TABLE IF EXISTS new_table;
CREATE TABLE new_table (
id INT,
birthDate DATE,
avgRating DOUBLE
) USING DELTA
```
- D. 
```sql
CREATE TABLE new_table (
id INT,
birthDate DATE,
avgRating DOUBLE
) USING DELTA
```
- E. 
```sql
ALTER TABLE IF EXISTS new_table RENAME TO old_table;
CREATE TABLE new_table (
id INT,
birthDate DATE,
avgRating DOUBLE
) USING DELTA
```

```{toggle}
Correct Answer: B. 

CREATE OR REPLACE TABLE new_table (
id INT,
birthDate DATE,
avgRating DOUBLE
) USING DELTA

Exam Topic: ELT with Spark SQL and Python

Explanation: The `CREATE OR REPLACE TABLE` command is used to create a new table with the specified schema, and it will replace any existing table with the same name. This ensures that the new table is created with the desired structure, even if a table with the same name already exists.

```

## Question 10

Which SQL command is used to add new rows to an existing Delta table?

- A. MERGE INTO
- B. LOAD DATA
- C. INSERT INTO
- D. UPSERT
- E. ADD ROWS

```{toggle}
Correct Answer: C. INSERT INTO
Exam Topic: Incremental Data Processing
Explanation: The `INSERT INTO` SQL command is used to append new rows to an existing table. This command is commonly used in data manipulation operations to add data to tables, including Delta tables in the Databricks environment.
```

## Question 11

A data engineering team is working with a Delta table and wants to ensure that their queries are as efficient as possible. They are particularly interested in optimizing the retrieval of recent data, which is queried most frequently. What optimization technique should they consider to prioritize the access to the most recent data?

- A. Partitioning by date
- B. Z-Ordering by date
- C. Data skipping based on date
- D. Increasing the shuffle partitions
- E. Decreasing the size of data files

```{toggle}
Correct Answer: A. Partitioning by date

Exam Topic: Incremental Data Processing

Explanation: Partitioning a Delta table by date allows the query engine to read only the relevant partitions that contain the recent data, thus reducing the amount of data scanned and improving query performance.

```

## Question 12

A data engineer wants to ensure that a database named `sales_data` is created only if it does not already exist in the metastore. The database should be located at the path `/data/sales_data`. Which command should the data engineer use?

- A. CREATE DATABASE sales_data LOCATION '/data/sales_data';
- B. CREATE DATABASE IF NOT EXISTS sales_data;
- C. CREATE DATABASE IF NOT EXISTS sales_data LOCATION '/data/sales_data';
- D. CREATE DATABASE IF NOT EXISTS sales_data DELTA LOCATION '/data/sales_data';
- E. CREATE DATABASE sales_data DELTA LOCATION '/data/sales_data';

```{toggle}
Correct Answer: C. CREATE DATABASE IF NOT EXISTS sales_data LOCATION '/data/sales_data';

Exam Topic: Databricks Lakehouse Platform

Explanation: The `CREATE DATABASE IF NOT EXISTS` command followed by the `LOCATION` clause ensures that the database is created only if it does not exist, and specifies the location where the database data should be stored.

```

## Question 13

A junior data engineer is tasked with creating a managed table named `employee_data` in Spark SQL, where Spark is responsible for managing both the data and metadata. Which command should the senior data engineer recommend?

- A. CREATE TABLE employee_data (id INT, name STRING) USING parquet OPTIONS (PATH "dbfs:/employee_data");
- B. CREATE MANAGED TABLE employee_data (id INT, name STRING) USING parquet OPTIONS (PATH "dbfs:/employee_data");
- C. CREATE MANAGED TABLE employee_data (id INT, name STRING);
- D. CREATE TABLE employee_data (id INT, name STRING) USING DBFS;
- E. CREATE TABLE employee_data (id INT, name STRING);

```{toggle}
Correct Answer: E

Exam Topic: ELT with Spark SQL and Python

Explanation: The `CREATE TABLE` command creates a table where Spark manages both the data and metadata. There is no need to specify the storage path as Spark will handle it internally.

```

## Question 14

A data engineer needs to define a logical structure that can be used to query data from multiple tables without physically storing the combined data. This structure should be accessible across different sessions. What should the data engineer create?

- A. View
- B. Temporary view
- C. Delta Table
- D. Database
- E. Spark SQL Table

```{toggle}
Correct Answer: A. view

Exam Topic: ELT with Spark SQL and Python

Explanation: A view is a logical structure that can be used to query data across multiple sessions without physically storing the data. It is session-scoped and will be dropped when the session ends.

```

## Question 15

A data engineering team is working with Parquet tables that are frequently updated with new data. They want to ensure that their queries reflect the most recent data without being affected by caching issues. What should they do to achieve this?

- A. Convert the tables to Delta format and enable auto-refresh
- B. Store the tables in a cloud-based storage system with versioning
- C. Refresh the table metadata after each update
- D. Disable caching for the tables
- E. Use streaming to continuously update the tables

```{toggle}
Correct Answer: C. Refresh the table metadata after each update

Exam Topic: Data Governance

Explanation: Refreshing the table metadata after each update ensures that the most recent data is available for queries, and it addresses the issue of stale cached data.

```

## Question 16

A data engineer is creating a new table `customer_summary` from an existing table `customer_details` using the following command:

```sql
CREATE TABLE customer_summary AS
SELECT customer_id,
SUM(purchase_amount) AS total_spent
FROM customer_details
GROUP BY customer_id;
```

A junior data engineer is curious about why there is no need to specify a schema for the new table. What is the correct explanation?

- A. The schema is automatically inferred from the result of the SELECT statement.
- B. The schema is copied from the source table `customer_details`.
- C. The schema is not required for tables created with the `CREATE TABLE AS SELECT` command.
- D. All columns in the new table are assumed to be of type STRING.
- E. The new table does not support a schema.

```{toggle}
Correct Answer: A. The schema is automatically inferred from the result of the SELECT statement.

Exam Topic: ELT with Spark SQL and Python

Explanation: When using the `CREATE TABLE AS SELECT` command, the schema for the new table is automatically inferred from the result of the SELECT statement.

```

## Question 17

A data engineer is considering the best approach to update a table with new data. They are debating whether to overwrite the existing table or to delete and recreate it. Which of the following is an incorrect reason to choose overwriting over deletion and recreation?

- A. Overwriting is more efficient as it does not require deleting files.
- B. Overwriting provides a cleaner history for logging and auditing.
- C. Overwriting preserves the old version of the data for Time Travel.
- D. Overwriting is an atomic operation, preventing the table from being left in an inconsistent state.
- E. Overwriting allows for schema evolution without the need to recreate the table.

```{toggle}
Correct Answer: B. Overwriting provides a cleaner history for logging and auditing.

Exam Topic: Production Pipelines

Explanation: Overwriting a table does not necessarily provide a cleaner history for logging and auditing. In fact, it may overwrite the history, whereas deleting and recreating a table could potentially provide a clearer demarcation in the table's history.

```

## Question 18

A data engineer wants to select unique records from a Delta table named `sales_records`. Which command will achieve this?

- A. DELETE DUPLICATES FROM sales_records;
- B. SELECT * FROM sales_records WHERE duplicate = False;
- C. SELECT DISTINCT * FROM sales_records;
- D. MERGE INTO sales_records USING (SELECT DISTINCT * FROM sales_records) AS unique_records ON true WHEN NOT MATCHED THEN INSERT *;
- E. MERGE INTO sales_records USING (SELECT DISTINCT * FROM sales_records) AS unique_records;

```{toggle}
Correct Answer: C. SELECT DISTINCT * FROM sales_records;

Exam Topic: ELT with Spark SQL and Python

Explanation: The `SELECT DISTINCT` command is used to return only distinct (unique) rows from a table, effectively removing duplicates.

```

## Question 19

A data engineer needs to join two tables, `orders` and `customers`, on a common column `customer_id`. The result should only include rows that have matching `customer_id` values in both tables. Which SQL command should be used?

- A. INNER JOIN
- B. FULL OUTER JOIN
- C. LEFT JOIN
- D. RIGHT JOIN
- E. CROSS JOIN

```{toggle}
Correct Answer: A. INNER JOIN

Exam Topic: ELT with Spark SQL and Python

Explanation: An INNER JOIN selects records that have matching values in both tables. It is the correct choice when you want to combine rows from two tables and only include the rows with matching keys.

```

## Question 20

A junior data engineer has a table `shopping_carts` with the following schema:

```
cart_id STRING,
items ARRAY<STRUCT<item_id:STRING, quantity:INT>>
```

They need to flatten the `items` array to create a new table with the schema:

```
cart_id STRING,
item_id STRING,
quantity INT
```

Which command should they use to achieve this?

- A. SELECT cart_id, items.item_id, items.quantity FROM shopping_carts;
- B. SELECT cart_id, explode(items) AS (item_id, quantity) FROM shopping_carts;
- C. SELECT cart_id, posexplode(items) AS (item_id, quantity) FROM shopping_carts;
- D. SELECT cart_id, explode_outer(items) AS (item_id, quantity) FROM shopping_carts;
- E. SELECT cart_id, inline(items) AS (item_id, quantity) FROM shopping_carts;

```{toggle}
Correct Answer: B. SELECT cart_id, explode(items) AS (item_id, quantity) FROM shopping_carts;

Exam Topic: ELT with Spark SQL and Python

Explanation: The `explode` function is used to explode an array of structs into a table with multiple rows, with each field of the struct becoming a separate column in the output.

```

## Question 21

A data engineer needs to flatten a nested JSON structure in a DataFrame `events_df` with the following schema:
```
event_id STRING,
details STRUCT<user_id:STRING, timestamp:TIMESTAMP, location:STRING>
```

The engineer wants to create a new DataFrame with the user_id and timestamp fields at the top level. Which command should be used?

- A. SELECT event_id, details.user_id, details.timestamp FROM events_df;
- B. SELECT event_id, flatten(details) FROM events_df;
- C. SELECT event_id, details['user_id'], details['timestamp'] FROM events_df;
- D. SELECT event_id, details.user_id as user_id, details.timestamp as timestamp FROM events_df;
- E. SELECT event_id, explode(details) FROM events_df;

```{toggle}
Correct Answer: D
Exam Topic: ELT with Spark SQL and Python
Explanation: The correct command to flatten the nested JSON structure and select the `user_id` and `timestamp` fields at the top level is to use the dot notation to access the fields within the `details` struct and alias them appropriately.

```


## Question 22

A data engineering team needs to automate a Spark SQL query that references a table with a date suffix in its name, such as `daily_metrics_20220101`. The date in the table name should be updated to the current date whenever the query is executed. Which approach should the team take?

- A. Use a PySpark script with string interpolation to dynamically construct the table name based on the current date.
- B. Create a scheduled job that manually updates the table name in the query each day.
- C. Modify the query to use a static table name without a date suffix.
- D. Implement a UDF (User-Defined Function) to generate the table name dynamically within the query.
- E. Use a configuration file to specify the table name, and update it daily before running the query.

```{toggle}
Correct Answer: A
Exam Topic: Production Pipelines
Explanation: The most efficient way to automate the process is to use a PySpark script with string interpolation to dynamically construct the table name based on the current date. This allows the query to be run automatically without manual intervention.

```


## Question 23

A data engineer needs to temporarily expose a PySpark DataFrame `sales_df` to SQL queries for a quick data exploration task. Which command should the engineer execute?

- A. sales_df.createOrReplaceTempView("temp_sales")
- B. sales_df.createGlobalTempView("temp_sales")
- C. sales_df.registerTempTable("temp_sales")
- D. sales_df.saveAsTable("temp_sales")
- E. sales_df.write.saveAsTable("temp_sales")

```{toggle}
Correct Answer: A
Exam Topic: Databricks Lakehouse Platform
Explanation: The `createOrReplaceTempView` method creates a temporary view that is session-scoped, allowing the data to be queried using SQL for the duration of the Spark session.

```


## Question 24

A data engineer is tasked with generating a dynamic table name in a Python script, where the table name is composed of a `region_code`, `store_number`, and `fiscal_year`. For example, if `region_code = "west"`, `store_number = "250"`, and `fiscal_year = "2022"`, the table name should be `west250_sales_2022`. Which Python command should the engineer use?

- A. `table_name = "{}{}{}_sales_{}".format(region_code, store_number, fiscal_year)`
- B. `table_name = region_code + store_number + "_sales_" + fiscal_year`
- C. `table_name = f"{region_code}{store_number}_sales_{fiscal_year}"`
- D. `table_name = "%s%s_sales_%s" % (region_code, store_number, fiscal_year)`
- E. `table_name = region_code.concat(store_number).concat("_sales_").concat(fiscal_year)`

```{toggle}
Correct Answer: C
Exam Topic: ELT with Spark SQL and Python
Explanation: The f-string (formatted string literal) in Python allows for easy and readable string interpolation, which is ideal for dynamically constructing strings like table names.

```


## Question 25

A data engineer is attempting to perform a streaming read from a Kafka source using the following code block:
```python
(spark
.readStream
.format("kafka")
.option("kafka.bootstrap.servers", "host1:port1,host2:port2")
.option("subscribe", "topic1")
.load()
)
```
The engineer encounters an error stating that the Kafka source is not found. Which of the following changes should be made to the code block to resolve the issue?

- A. Replace `.format("kafka")` with `.format("org.apache.spark.sql.kafka010")`.
- B. Add `.option("startingOffsets", "earliest")` after the `.option("subscribe", "topic1")` line.
- C. Add `.option("kafka.metadata.broker.list", "host1:port1,host2:port2")` after the `.format("kafka")` line.
- D. Replace `.readStream` with `.read` to perform a batch read instead.
- E. Add `.option("failOnDataLoss", "false")` after the `.option("subscribe", "topic1")` line.

```{toggle}
Correct Answer: A
Exam Topic: Incremental Data Processing
Explanation: The error indicates that the Kafka source is not correctly specified. The format for Kafka in Spark Structured Streaming should be the fully qualified class name `org.apache.spark.sql.kafka010`.

```


## Question 26

A data engineer is setting up a Structured Streaming job to process data from a Delta Lake table and write the results to another Delta Lake table. The engineer wants to process all available data in a single batch and then stop the stream. Which line of code should be used to configure the trigger for the streaming query?

- A. `.trigger(once=True)`
- B. `.trigger(availableNow=True)`
- C. `.trigger(processingTime='0 seconds')`
- D. `.option("maxFilesPerTrigger", 1)`
- E. `.trigger(maxOffsetsPerTrigger=1)`

```{toggle}
Correct Answer: A
Exam Topic: Production Pipelines
Explanation: The `trigger(once=True)` option in Structured Streaming allows the query to process all available data in a single batch and then stop.

```


## Question 27

A data engineer needs to process only new files that have been added to a directory since the last pipeline run. The directory is shared with other systems, so files cannot be moved or deleted. Which Databricks feature should the engineer use to identify and ingest only the new files?

- A. Databricks Delta Lake
- B. Databricks Job Scheduler
- C. Databricks File System (DBFS)
- D. Databricks Auto Loader
- E. Databricks Structured Streaming

```{toggle}
Correct Answer: D
Exam Topic: Incremental Data Processing
Explanation: Databricks Auto Loader provides a mechanism to incrementally and efficiently process new files in a directory without the need to move or delete them.

```


## Question 28

A data engineering team is updating their data ingestion pipeline to use Databricks Auto Loader for incremental loading of CSV files. The current code block is as follows:

```python
(spark.readStream.format("cloudFiles")
.option("cloudFiles.format", "csv")
.option("cloudFiles.schemaLocation", schemaLocation)
.load(sourcePath))
```

Which of the following changes is necessary to ensure the code block correctly uses Auto Loader for ingesting CSV files?

- A. No change is required; the code block already uses Auto Loader with the `cloudFiles` format.
- B. Change `.format("cloudFiles")` to `.format("csv")`.
- C. Add `.option("header", "true")` after the `.option("cloudFiles.format", "csv")` line.
- D. Add `.option("inferSchema", "true")` after the `.option("cloudFiles.format", "csv")` line.
- E. Replace `.load(sourcePath)` with `.autoLoader(sourcePath)`.

```{toggle}
Correct Answer: A
Exam Topic: Incremental Data Processing
Explanation: The `cloudFiles` format in the code block is the correct format for using Auto Loader in Databricks to ingest CSV files incrementally.

```


## Question 29

Which of the following data workloads typically uses a Bronze table as its source?

- A. A job that performs data deduplication and quality checks on raw data
- B. A job that generates business reports from curated data
- C. A job that applies complex transformations to prepare data for machine learning models
- D. A job that performs real-time analytics on processed data
- E. A job that exports data to external systems for further processing

```{toggle}
Correct Answer: A
Exam Topic: Data Governance
Explanation: A Bronze table in a data lakehouse architecture typically contains raw data. Jobs that perform initial data cleaning, deduplication, and quality checks would use a Bronze table as their source.

```


## Question 30

Which of the following data workloads is most likely to use a Silver table as its source?

- A. A job that performs initial parsing and validation of raw log files
- B. A job that aggregates data to generate daily sales reports
- C. A job that ingests streaming data into the data lakehouse
- D. A job that refines raw data by applying business logic and filtering out bad records
- E. A job that exports curated data to a data warehouse for business intelligence

```{toggle}
Correct Answer: D
Exam Topic: Data Governance
Explanation: A Silver table in a data lakehouse architecture typically contains refined data that has been cleaned and processed to apply business logic. Jobs that refine raw data by applying business logic and filtering out bad records would use a Silver table as their source.

```



## Question 31

Which of the following Structured Streaming queries is correctly calculating the maximum temperature recorded each day for a stream of sensor data?

- A.
```
(spark.readStream
    .schema(sensorDataSchema)
    .parquet(sensorDataPath)
    .groupBy(window(col("timestamp"), "1 day"))
    .max("temperature")
    .writeStream
    .option("checkpointLocation", checkpointPath)
    .outputMode("complete")
    .start("dailyMaxTemperatures")
)
```
- B.
```
(spark.readStream
    .schema(sensorDataSchema)
    .parquet(sensorDataPath)
    .select("timestamp", "temperature")
    .writeStream
    .option("checkpointLocation", checkpointPath)
    .outputMode("update")
    .start("dailyTemperatures")
)
```
- C.
```
(spark.read
    .schema(sensorDataSchema)
    .parquet(sensorDataPath)
    .groupBy(window(col("timestamp"), "1 day"))
    .max("temperature")
    .writeStream
    .option("checkpointLocation", checkpointPath)
    .outputMode("complete")
    .start("dailyMaxTemperatures")
)
```
- D.
```
(spark.readStream
    .schema(sensorDataSchema)
    .parquet(sensorDataPath)
    .withColumn("temperature", col("temperature").cast("double"))
    .writeStream
    .option("checkpointLocation", checkpointPath)
    .outputMode("append")
    .start("temperatureCasts")
)
```
- E.
```
(spark.readStream
    .schema(sensorDataSchema)
    .parquet(sensorDataPath)
    .filter(col("temperature").isNotNull)
    .writeStream
    .option("checkpointLocation", checkpointPath)
    .outputMode("append")
    .start("validTemperatures")
)
```

```{toggle}
Correct Answer: A

Exam Topic: Incremental Data Processing

Explanation:
Option A is the correct answer because it reads from a stream (`readStream`), groups the data by day using a windowing function (`groupBy(window(col("timestamp"), "1 day"))`), calculates the maximum temperature for each day (`max("temperature")`), and writes the output in complete mode, which is necessary for windowed aggregations that update the full result set as new data arrives.
```

## Question 32

What feature does Delta Lake not provide to ensure data quality and reliability in ELT pipelines?"

- A. Support for ACID transactions
- B. Built-in data quality constraints
- C. Automatic handling of schema evolution
- D. Real-time anomaly detection in data streams
- E. In-memory data caching for faster processing

```{toggle}
Correct Answer: D

Exam Topic: Incremental Data Processing

Explanation:

Real-time anomaly detection in data streams - This feature is typically not a direct capability of Delta Lake. While Delta Lake provides robust support for ACID transactions, built-in data quality constraints, and automatic handling of schema evolution to ensure data quality and reliability, real-time anomaly detection in data streams generally requires additional analytics or machine learning tools integrated into the data pipeline. Delta Lake focuses on storage, transactional integrity, schema management, and other aspects of data reliability and quality rather than real-time data stream analysis.
```

## Question 33

A data engineer wants to prioritize certain transformations over others in a Delta Live Tables pipeline due to resource constraints. How can this be achieved?

- A. Use the `@dlt.expectation` decorator to define priority levels.
- B. Manually execute each transformation in the desired order.
- C. Define priority levels in the DLT pipeline's configuration file.
- D. Use the `@dlt.table` decorator to specify priorities between transformations.
- E. Create separate DLT pipelines for each transformation with different priorities.

```{toggle}
Correct Answer: C

Exam Topic: Production Pipelines

Explanation:

Defining priority levels in the DLT pipeline's configuration file allows the data engineer to control the order in which transformations are executed based on resource constraints and dependencies, ensuring that critical transformations are processed first.
```

## Question 34

When defining a Delta Live Tables (DLT) pipeline, how do you correctly specify the creation of a live table based on data ingested from a CSV file?

- A. Utilize the `CREATE TABLE` statement in DLT SQL with the CSV file as the source.
- B. Use the DLT Python API to read the CSV file and declare the output as a live table.
- C. Directly reference the CSV file path in the TABLE definition without any specific API or function.
- D. Implement a custom DLT function `dlt.read_csv("path/to/csv")` for reading CSV files and creating live tables.
- E. Configure the CSV file as a streaming source using DLT's built-in connectors.

```{toggle}
Correct Answer: B

Exam Topic: Incremental Data Processing

Explanation:

DLT does not directly expose a function like dlt.read_csv(...) for ingesting CSV files into live tables nor does it allow prefixing paths with dlt. or using specific SQL syntax like CREATE OR REPLACE LIVE TABLE within its framework for this purpose. 
```

## Question 35

In a Delta Live Tables pipeline, a dataset is defined with the following data quality expectation:
```
CONSTRAINT valid_email EXPECT (email LIKE '%@%.%')
```
What happens when a batch of data containing records with invalid email formats is processed?

- A. Records with invalid email formats are dropped and recorded as invalid in the event log.
- B. Records with invalid email formats are added to the dataset and marked as invalid in the event log.
- C. The entire batch fails and no records are added to the dataset.
- D. Records with invalid email formats are added to the dataset without a warning in the event log.
- E. Records with invalid email formats are sent to a quarantine table for further investigation.

```{toggle}
Correct Answer: B

Exam Topic: Incremental Data Processing

Explanation:

This answer reflects the default action of warn where invalid records (in this case, records with invalid email formats) are written to the target dataset, and the failure (non-compliance with the expectation) is reported as a metric for the dataset, allowing users to track and address data quality issues without preventing the ingestion of data into the dataset.
```

## Question 36

What is the behavior of a Delta Live Tables pipeline in Development mode with Triggered Pipeline Mode when it is started with valid definitions and unprocessed data?

- A. The pipeline updates all datasets once and then enters a paused state, retaining compute resources.
- B. The pipeline continuously updates datasets until manually stopped, retaining compute resources.
- C. The pipeline updates datasets at set intervals until manually stopped, releasing compute resources after each update.
- D. The pipeline updates all datasets once and then shuts down, releasing compute resources.
- E. The pipeline updates datasets at set intervals until manually stopped, retaining compute resources.

```{toggle}
Correct Answer: D

Exam Topic: Production Pipelines

Explanation:

In Development mode with Triggered Pipeline Mode, when the pipeline is started, it processes the available data once, updates all datasets, and then shuts down. Compute resources are released after the pipeline shuts down.
```

## Question 37

What strategy can a data engineer employ to ensure nightly job completion while minimizing compute costs when a task in a multi-task job fails intermittently?

- A. Allocate a dedicated cluster for each task in the job.
- B. Set a retry policy specifically for the task that fails intermittently.
- C. Schedule multiple runs of the job to increase the chance of completion.
- D. Monitor the task in real-time to identify the cause of failure.
- E. Set a retry policy for the entire job.

```{toggle}
Correct Answer: B

Exam Topic: Production Pipelines

Explanation:

Setting a retry policy specifically for the task that fails intermittently allows the job to attempt to rerun only the failed task without having to restart the entire job. This minimizes compute costs by not unnecessarily rerunning successful tasks.
```

## Question 38

To avoid failures in a dependent job caused by the first job not completing on time, what should a data engineer implement?

- A. Use cluster pools to improve job efficiency.
- B. Implement a retry policy for the first job to ensure faster completion.
- C. Combine both jobs into a single job with task dependencies.
- D. Configure the data to be streamed between the two jobs.
- E. Reduce the output size of the second job to prevent failures.

```{toggle}
Correct Answer: C

Exam Topic: Production Pipelines

Explanation:

Combining both jobs into a single job with task dependencies ensures that the second task (previously the second job) does not start until the first task (previously the first job) has successfully completed. This eliminates the issue of the second job starting before the first job has finished.
```

## Question 39

How can a data engineer version control a complex job schedule in Databricks?

- A. Export the job's XML configuration from the job's settings page.
- B. Run the job once on an all-purpose cluster.
- C. Link the job to notebooks in a Databricks Repo.
- D. Export the job's JSON configuration from the job's settings page.
- E. Run the job once on a job cluster.

```{toggle}
Correct Answer: D

Exam Topic: Production Pipelines

Explanation:
Exporting the job's JSON configuration from the job's settings page allows the data engineer to version control the job schedule. The JSON file can be committed to a version control system like Git, enabling tracking of changes and rollback if necessary.
```

## Question 40

What action can the data engineering team take to improve the latency of a data analyst's Databricks SQL queries if all queries use the same SQL endpoint?

- A. Enable the Auto Stop feature for the SQL endpoint.
- B. Enable the Serverless feature for the SQL endpoint.
- C. Increase the size of the SQL endpoint's cluster.
- D. Increase the maximum bound of the SQL endpoint's auto-scaling range.
- E. Enable the Serverless feature and adjust the Spot Instance Policy to "Cost Optimized."

```{toggle}
Correct Answer: D

Exam Topic: Databricks Lakehouse Platform

Explanation:
Increasing the maximum bound of the SQL endpoint's auto-scaling range allows the endpoint to scale up to a larger size when needed, which can improve the performance and reduce the latency of the queries.

```


## Question 41

How can a manager automate the daily update of the results of a Databricks SQL query without manual intervention?

- A. Schedule the query to run every day from the Jobs UI.
- B. Schedule the query to refresh daily from the query's page in Databricks SQL.
- C. Schedule the query to run every 12 hours from the Jobs UI.
- D. Schedule the query to refresh daily from the SQL endpoint's page in Databricks SQL.
- E. Schedule the query to refresh every 12 hours from the SQL endpoint's page in Databricks SQL.

```{toggle}
Correct Answer: B

Exam Topic: Databricks Lakehouse Platform

Explanation:
Scheduling the query to refresh daily from the query's page in Databricks SQL allows the manager to automate the query execution and ensure that the results are updated each day without manual rerunning.
```

## Question 42

What can the data engineering team do to be notified if an ELT job has not run in over an hour?

- A. Set up an Alert for the dashboard to notify them if the runtime exceeds 60 minutes.
- B. Set up an Alert for the query to notify when the ELT job fails.
- C. Set up an Alert for the dashboard to notify when it has not refreshed in 60 minutes.
- D. Set up an Alert for the query to notify them if the runtime exceeds 60 minutes.
- E. This type of alerting is not supported in Databricks.

```{toggle}
Correct Answer: C

Exam Topic: Databricks Lakehouse Platform

Explanation:

Setting up an Alert for the dashboard that monitors the ELT job's runtime can notify the data engineering team if the dashboard has not refreshed in 60 minutes, indicating that the job has not run within the expected timeframe.
```

## Question 43

Which of the following is NOT a reason why a Databricks SQL dashboard might take a few minutes to update?

- A. The SQL endpoint used by the queries may need time to start up.
- B. The queries themselves may take a few minutes to execute.
- C. The dashboard's queries may be waiting for their own clusters to start.
- D. The job updating the dashboard may be using a non-pooled endpoint.
- E. The dashboard is configured to check for new data before updating.

```{toggle}
Correct Answer: E

Exam Topic: Databricks Lakehouse Platform

Explanation:
The reason that the dashboard is configured to check for new data before updating does not explain a delay in the dashboard update. The other options are valid reasons for a delay, such as startup time for endpoints or clusters, or the inherent runtime of the queries.
```

## Question 44

To grant a new data engineer the ability to query a specific table, which SQL command should be used?

- A. GRANT SELECT ON TABLE sales TO 'new.engineer@company.com';
- B. GRANT USAGE ON TABLE sales TO 'new.engineer@company.com';
- C. GRANT SELECT ON DATABASE retail TO 'new.engineer@company.com';
- D. GRANT SELECT ON TABLE sales TO USER 'new.engineer@company.com';
- E. GRANT READ ON TABLE sales TO 'new.engineer@company.com';

```{toggle}
Correct Answer: D

Exam Topic: Data Governance

Explanation:
The correct SQL command to grant a user the ability to query a specific table is `GRANT SELECT ON TABLE sales TO USER 'new.engineer@company.com';`. This grants the SELECT permission on the table `sales` to the user with the specified email address.
```

## Question 45

To grant a new data engineer full permissions on a table for an ELT project, which SQL command should be used?

- A. GRANT ALL PRIVILEGES ON TABLE sales TO 'new.engineer@company.com';
- B. GRANT ALL ON TABLE sales TO 'new.engineer@company.com';
- C. GRANT ALL PRIVILEGES ON DATABASE retail TO 'new.engineer@company.com';
- D. GRANT ALL ON TABLE sales TO USER 'new.engineer@company.com';
- E. GRANT CONTROL ON TABLE sales TO 'new.engineer@company.com';

```{toggle}
Correct Answer: A

Exam Topic: Data Governance

Explanation:
The correct SQL command to grant a user full permissions on a table is `GRANT ALL PRIVILEGES ON TABLE sales TO 'new.engineer@company.com';`. This grants all available privileges on the table `sales` to the user with the specified email address, allowing them to fully manage the table.
```