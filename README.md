<p>
    <h1 align="center">Data Representation & Querying - Big Project</h1>
    <p align="center"><img align="center" src='staticpages/img/GMIT.jpg' width=40%/></p>
    <h3 align="center">Student: Eoghan Delaney</h3>
    <h3 align="center">Student Number: G00376462</h3>
</p>

## My Project
<p>My project consisted of creating a REST API with a web interface, consuming data from Twitters API and Google Maps API. The theme of the REST API was to highlight crime, geographically in Ireland.</p>

Below is a live link of the REST API.
<p><a href ="http://dellaa87.pythonanywhere.com/index.html">http://dellaa87.pythonanywhere.com/index.html</a></p>

<p>All the crimes are shown on a Google Map, utilising the API. When logging a crime the user can select the location on a Google Map. Google Maps API requires an authentication key which is included in the API script. All logged crimes are then displayed in the form of a table and on the maps.</p>

<p>As part of this project I used Twitter's API to get tweets relating to Crime in Ireland. Twitter uses four authentication keys to enable users to consume the API - consumer_key, consumer_secret, access_token, access_secret. This information was stored in a separate password file. This File is not included on the Repository - using a Gitignore file. </p>

## Libraries 
I have used multiple libraries as part of this submission and these are all listed in my requirements file. Some of the packages include.

1.  Tweepy - A Python library used to interact with Twitter API.
2.  mysqlclient - A Python package for interacting with SQL databases.

