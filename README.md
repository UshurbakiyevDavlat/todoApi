# todoApi
Django rest framework, example for learning  

With a minimal amount of code Django REST Framework has allowed us to create a Django API
from scratch. Unlike our example in the previous chapter, we did not build out any web pages
for this project since our goal was just to create an API. However at any point in the future, we
easily could! It would just require adding a new view, URL, and a template to expose our existing
database model.
An important point in this example is that we added CORS headers and explicitly set only the
domains localhost:3000 and localhost:8000 to have access to our API. Correctly setting CORS
headers is an easy thing to be confused about when you first start building APIs.
There’s much more configuration we can and will do later on but at the end of the day creating
Django APIs is about making a model, writing some URL routes, and then adding a little bit of
magic provided by Django REST Framework’s serializers and views.
