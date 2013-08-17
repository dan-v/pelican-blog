Crossfit Gym Review Site 
###########################

:date: 2012-11-20 15:00
:tags: flask,crossfit,python
:category: Project
:author: Dan

A random idea to build a site to review Crossfit gyms. I took this as an opportunity to play with a new web framework, Flask, that I had wanted to take a look at for some time. I liked the idea of a lightweight framework after dealing mostly with Django in the past.

I found these series of articles_ by Miguel Grinberg to be very useful in jumpstarting the project.

.. _articles: http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database

I wrote a hacky python script_ to scrape all of the data for Crossfit affiliates including gym name, website, address, phone number, and coordinate location on a map. Once all the data could be scraped it was time to build the application.

.. _script: https://github.com/dan-v/crossfitboxreview/blob/master/seed_affiliates.py

On the backend, I built out some very barebones models and views for reviewing gyms and inserted all the affiliate records with the script mentioned above.

On the frontend, I used Twitter Bootstrap and took the map application that Crossfit already had (map.crossfit.com_) and remodeled it for this website. I expanded the map, rebuilt the search, and added custom dialogs that pulled details from the database.

.. _map.crossfit.com: http://map.crossfit.com

I ended up hosting it on Heroku (crossfitboxreview.herokuapp.com_). Website source can be found at Github_.

.. _crossfitboxreview.herokuapp.com: http://crossfitboxreview.herokuapp.com/
.. _Github: https://github.com/dan-v/crossfitboxreview
