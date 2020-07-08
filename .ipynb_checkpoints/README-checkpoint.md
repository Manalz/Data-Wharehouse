A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They need building an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to. The database and ETL pipeline are tested by running the given queries the analytics team from Sparkify and compare the results with their expected results.

There are two datasets that reside in S3. Here are the S3 links for each:

Song data: s3://udacity-dend/song_data
Log data: s3://udacity-dend/log_data

The song and log datasets are used for the project database. A star schema is chosen to be optimized for queries on song play analysis. This includes the following tables:

Fact Table:
    - songplays - records in log data associated with song plays i.e. records with page NextSong
      songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
Dimension Tables:
   - users - users in the app
      user_id, first_name, last_name, gender, level
   - songs - songs in music database
      song_id, title, artist_id, year, duration
   - artists - artists in music database
       artist_id, name, location, latitude, longitude
   - time - timestamps of records in songplays broken down into specific units
       start_time, hour, day, week, month, year, weekday

The project repository contains the following files:

    1. 'create_table.py' is where can create your fact and dimension tables for the star schema in Redshift.
    2. 'etl.py' is where you'll load data from S3 into staging tables on Redshift and then process that data into  your analytics tables on Redshift.
    3. 'sql_queries.py' is where can define you SQL statements, which will be imported into the two other files above.
    4. 'IaC.ipynb' is where you can launch and delete a redshift cluster and create an IAM role that has read access to S3.
    5. 'dwh.cfg' is where you can add redshift database and IAM role info. 
       
       
To run the project, you should perform the following steps:
    1. run cells in 'IaC.ipynb' from step1 up to step4 to create IAM role and launch the redshift cluster.
    2. run create_tables.py in Terminal to create the tables using command 'python create_tables.py'. 
    3. run etl.py in Terminal to copy data from S3 files into staging tables and insert data into the tables. Use command 'python etl.py'
    4. Don't forget to delete the cluster and clear data by running step5 in 'IaC.ipynb'.
 
 