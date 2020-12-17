# Shop_Engine

A small business website scraper django based search engine

## Purpose of website

Create a way for searching products of only small businesses via their own websites. Bypassing any and all affiliate links and fees.

## Rundown of Website

### Web Server
A Django Backend is used as the framework with a SQL database used to manage all information.
All design and static code done with HTML, CSS, and JQuery.

### Web Scraping
Web scraping is done via Beautiful Soup and LXML to gain product info from websites.
Parameters for search built into SQL database which is updated via django admin
Web Scraping Script accesible through /SearchStore/management/commands/scrape.py

## Running Instructions

### Setup
1 - Install requirements
````
$ pip install -r requirements.txt
````
2 - Configure the database
````
$ python manage.py migrate
````
3 - Configure the admin
````
$ python manage.py createsuperuser
````
### Start the project.

In order to run Django
````
$ python manage.py runserver
````
