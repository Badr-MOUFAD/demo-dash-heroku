# Demo dashboard

A demo dashboard to share the result of the clustering of Moroccan weather data. 

The Dashboard contains a spatiotemporal map of the clusters of the Maroccan regions.


# Steps to create/deploy a dash app

1. Run `py -m ven ven` to initialize a new virtual environment.

2. Run `.\venv\Scripts\activate` to activate the environment.

3. Install python packages mainly **dash** and **gunicorn**.

4. Create **Procfile** (essential file for Heroku)

    Within it write `web: gunicorn <name-of-the-entry-file-to-the-app>: server`
    
    In my case name of the entry file to the app is **app**

5. In `app.py` add the line of code `server = app.server`.

6. Add a `requirements.txt` where you list all app dependencies (packages)

    By running the command `pip freeze > requirements.txt` this file is created automatically