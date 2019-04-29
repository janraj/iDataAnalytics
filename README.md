# iDataAnalytics
This tools helps to get the data usage of your quay.io repository activities.
This requires token and API as input which must be passed through the .env file.
It find out which organization has downloaded the image from your repository and generate report including that.

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
