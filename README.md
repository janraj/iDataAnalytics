# iDataAnalytics
This tools helps to get the data usage of your quay.io repository activities.
This requires token and API as input which must be passed through the .env file.
It find out which organization has downloaded the image from your repository and generate report including that.

# Set the enviornment Variable 
  Following env variables are required now to form the report.
  ```
      DATA_ENDPOINT: You have to give full API where from we can get the Data
      DATA_ENDPOINT_KEY: Here You have to  provide teh Authentication required for the Tool to download data
      DATA_ENDPOINT_FILTER_TODAY = "?endtime="
      OUTPUT_FILE_NAME = Name of the report tag
      DATA_ENDPOINT_KEY = Key for the API.
  ```


# How to Run As Cron job
  If we want to run this as cron job try 
  ```	
	python main.py
  ```

# How to run and Generate report
  Run the following to generate weekly report 
  ```
  python report.py  
  ```
