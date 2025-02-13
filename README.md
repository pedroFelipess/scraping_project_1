# scraping_project_1
Data Monitoring Scraping with Python.

This code was created to monitor a computer case on Amazon, but it would work for tracking any product on Amazon.

## main.py
Here is the main file that will manage the entire scraping process and determine when the emails should be sent.

## send_email.py
This is the file responsible for formatting and sending emails. I chose to write the email-sending code in a separate file purely for organization, but it would still work if I did everything in "main.py".

## index.html
I chose to create an `index.html` file to design and customize the body of the emails that will be sent.

## Automation
There are several ways to make your code run periodically to monitor your product. In my case, I am using Railway to execute the code once a day, meaning I am monitoring the product daily via the cloud.