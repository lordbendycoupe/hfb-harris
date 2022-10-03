# How this project works
To use this project just clone the repo and run the ex.py code which will write and save 3 files as shown in the repo. Or, in the Jupyter Notebook
run the last cell and it'll do the same as the .py. 

# This project as a microservice
To showcase what this project could look like in a live setting I set up a basic microservice workflow. To achieve the same results above,
you can send a GET request to the REST API I set up which will invoke a Lambda function containing this script. The csv files
will be written and saved to an S3 bucket, which could then be attached to a lightsail or ec2 instance. 
Here is a screenshot of the API response in Postman. The way I have it set up right now it only outputs the raw response from the Census API.
![postman](https://user-images.githubusercontent.com/95596805/193510680-f0d711a9-3930-43da-b66b-3a4b653537ee.png)

Also here is an example of one of the API's resources, and the s3 bucket with csv files:
![lambda](https://user-images.githubusercontent.com/95596805/193505836-5699c7f1-61dc-4ca7-baa7-97d704462f73.png)
![s3](https://user-images.githubusercontent.com/95596805/193505840-4f673547-98c6-4bb0-baa5-dfc1d55f7059.png)

# Workflow (example: lightsail) 
![plant](https://user-images.githubusercontent.com/95596805/193507659-482abf63-7724-48df-8f01-2e1653ff6789.png)

# Quick explanation of the code
I noticed the http url for the Census API was somewhat convoluted so I decided to construct the links as objects with
elements of the url as attributes. The reason being just for simplicity, readability and orginization. It's eaiser to see what 
constitutes the request and what happens to the API response. Since this script must do three different requests I created one class per request since
the url varies. 

# Dependencies: 
Pandas
Numpy
Requests 



