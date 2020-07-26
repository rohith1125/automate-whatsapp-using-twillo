# Automating WhatsApp Using Twillo

This is a brief overview of the Twillo API. We will be automating WhatsApp messages.

Firstly, we need the following things installed on our PC to get started,
## Prerequisites:
* Python
* Git
* A task Scheduler
* Any IDE (Prefarabily Visual Studio Code, Sublime Text, Etc.)

We also need a web hosting service to send the messages automatically,

There are many services available to get this done, few of them are listed below,
* Back4app
* Firebase
* Google App Engine
* Heroku
* Elastic Beanstalk (AWS)

I'll be using Heroku for this,


Heroku is a cloud platform as a service supporting several programming languages. (Of Course including Python)


# Procedure
As we use twillo for the automation purpose, we are supposed to create a Twilio account.
After successfully creating the account we must log into the twillo account.
Now we will see the twillo dashboard which looks something like,


![Test Image 2](https://github.com/rohith1125/automate-whatsapp-using-twillo/blob/master/2.PNG)



Now we must navigate to the WhatsApp Section of the site,



![Test Image 1](https://github.com/rohith1125/automate-whatsapp-using-twillo/blob/master/1.PNG)



Now we must send the following message via WhatsApp to the number displayed on the twillo site from the device(the device on which we intend to receive the automated messages)
```
join valley-live
  ```
This initiates the request and confirms the message.
  And now we have the option to do certain things like,
  
  
 * Setting Appointment reminders
  * order notifications
  * Verification codes
  
  
 We select the appointment reminder option,
  Now the page looks like this
  
  ![Test Image 3](https://github.com/rohith1125/automate-whatsapp-using-twillo/blob/master/3.PNG)


  It has a simple User-Interface, 
  
  it asks for the senders and receivers phone numbers we need to fill them accordingly,
  It also has the Body to enter Your message and on clicking on make a request, the message will be sent to that sandbox.
  
  
  ![Test Image 5](https://github.com/rohith1125/automate-whatsapp-using-twillo/blob/master/Capture.PNG)
  
    
  ## Making this local :
  We achieve this by writing a python script in the IDE using the code displayed on the twillo side,
  
  ```
  from twilio.rest import Client 
 
account_sid = '' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your appointment is coming up on July 21 at 3PM',      
                              to='whatsapp:target number' 
                          ) 
 
print(message.sid)
```
  To run this code locally, we need to install the twillo dependency on our machine using,
  ```
  pip install twillo
  ```
  This will install twillo on our machine.
  So now, we can run this code locally.
  
   Now, We modify the code and create a function called send_msg() to call the message into the automation script.
   ```
    def send_msg():
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='The message you want to send',      
                              to='whatsapp:target phone number' 
                          ) 
 
print(message.sid)
```
  # Automation Part :
  We will use Advanced Python scheduler to automate the process of sending the messages.
  https://apscheduler.readthedocs.io/en/stable/userguide.html
  This is the link to the Documentation of the apscheduler.
  
  We start off by installing this package using the following command in the terminal,
  ```
  pip install apscheduler
  ```
  There are many options to choose from some of them are,
  ```
date: use when you want to run the job just once at a certain point of time
interval: use when you want to run the job at fixed intervals of time
cron: use when you want to run the job periodically at a certain time(s) of day
  ```
We can choose from the options accordingly,
I'll be using the interval option for this demonstration, in order to use this function we need to take the following code from their website,
```
from datetime import date

from apscheduler.schedulers.blocking import BlockingScheduler
from auto import send_msg
sched = BlockingScheduler()
sched.add_job(job_function, 'interval',hours=2)
sched.start()
```
We use this piece of code and create a .py file with the same directory as earlier,
we link the two files by calling the function which we created for this purpose earlier,
```
from auto import send_msg
```

 ![Test Image 6](https://github.com/rohith1125/automate-whatsapp-using-twillo/blob/master/Capture1.PNG)


Now we can send the messages at an interval of every 2 hours,
But we can't run the script locally always; 
  
This is where Heroku comes in, it'll make our code run until the servers are down(jk)
Heroku is a service to host our apps.

# Web Hosting part:
Firstly we must create a Heroku account and then we must install the Heroku CLI using,
  ```
  sudo snap install --classic Heroku
  ```
  From the Heroku CLI, we must log in to the account from the CLI using the command,
  ```
  Heroku login
  ```
  Now we need to list out the dependencies involved,
  
  * Twillo 
  * Apscheduler
  
  We must also add the software versions of the dependencies in a file info.txt for the sake of the server.
  We must also create a Procfile with the following text,
  ```
  clock: python clock.py
  ```
  The rest of the procedure (like initializing git etc.) needs to be done using the following commands,
  ```
  git init
  heroku git:remote -a auto
 ```
  ## To deploy the Application :
  ```
  git add .
  git commit -am "latest."
  git push Heroku master
  ```
  Finally, we need to enable the Dynos option to make it work automatically.
   
  
