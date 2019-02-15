# UrTracker
Django based Wellness tracker.  

The purpose is to track my well being and see if there is any correlation with use of particular supplements, a SAD Lamp, or exercise. 


# Set up

Ensure that you have docker desktop running on your lcoal machine. clone the repo and navigate to the main project directory and urn this command:

`docker-compose up --build`

Docker will run the build, once the set up is done, you can navigate to localhost:8000 to navigate through the application and signup

# Future Features
I want to add some kind of front end and make it a little easier to use. I would like a automated way of reminding me to input my data. 

My hope is that the front end will also give a visualization of the year overall

- [X] Create working connection to ES instance
- [ ] automated input gathering/reminders
- [X] Front end for input
- [X] visualization of data
- [ ] Add Elasticsearch functions for text purposes
- [ ] Add Drilldown information
- [ ] Correlation of different factors to rating
