from fastapi import FastAPI


# creating an instance
app = FastAPI()

@app.get('/')
def hello():
    return {"data":{'status':"success"}}

# $ steps to create an API
# import fastapi
# create an instance
# create the function
# decorate the function

@app.get('/about')
def about():
    return {"data":{"This is the about page"}}


# blog list
# @app.get('/blog')
# def blog():
    
#     return {'data': 'Blog List Page'}

 # WORKING WITH QUERY PARAMETERS
@app.get('/blog')
def blog(limit,published:bool = True,sort:str = None):
   

    # http://127.0.0.1:8000/blog?limit=50
    # http://127.0.0.1:8000/blog?limit=50&published=true
    # To only get 10 blogs ,cus having to display thousands of blogs at once would be inefficient
    if published:
        return {'data': f'{limit} published blogs'}
    else:
        return {'date': 'All blogs'}
    



@app.get('/blog/unpublished_blog')
def unpublished_blog():
    return {'data': 'All unpublished blogs'}


# To get a single item from the blog list
@app.get('/blog/{id}')
def blog(id:int):
    return {'data':id }

# Dynamic routes should be placed below static routes because 
# FastAPI evaluates routes in order. If a dynamic route is defined first,
#  it may capture requests intended for more specific static routes,
#  causing unexpected behavior


#  USING THE POST METHOD
# Inoder to get request from client(browser) we first need to
# import BaseModel from pydantic 
# use a class to define the parameters you need

# DEMOSTRATE THE USE OF POST METHOD
# @app.post('/blog')
# def create_blog():
#     return {'data': "Blog is created"}

from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]


@app.post('/blog')
def create_blog(request:Blog):
    return {'data': "Blog is created"}