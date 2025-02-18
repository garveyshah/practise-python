# Django Turorial

Django is a back-end server side web framework.
Django is free, open source and written in Python.
Django makes it easier to build web pages using Python.
Django was invented by Lawrence Journal-World in 2003, to meet the short deadlines 

# Objectives
1. Learn how to install and create a Django project.
2. Learn to create a project where you can add, update or delete data.
3. Mkaing HTML Templates and use Django Template Tags to insert data within a HTML document.
4. How to work with QuerySets to extract, filter, and sort data from the database.
5. Setting up a PostresSQL database and how to deploy your Django project to the world.

## What is Django?
- Django is a Python framework that makes it easier to create web sites using python.
- It emphasizes reusability of components, also referred to as DRY( Don't Repeat Yourself), and comes with ready ready-to-use features like login system, database connection and CRUD operations (CREATE READ UPDATE DELETE).

`Django is especially helpful for database driven websites.

## How does Django Work?
Django follows the MVT design patter  (Model View Template).
+ Model - The data you want to present, usually data from a database.
+ View - A request handler that returns the relevant template and content - based on the request from the user.
+ Template - A text file (like an HTML file) containing the layout of the web page, with logic on how to display the data.

### Model 
- Provides data from the database.
- The data os delivered as an Object Relational Mapping(ORM), which is a technique designed to make it easier to work with databases.
- The models are usually located in a file called `models.py`

### View 
A view is a function or method that takes http requests as arguments, imports the relevant models(s), and finds out what data to send to the tamplate, and returns the final result.
- Located in a file called `views.py`.
### Template
- Is a file where you describe how the result should be represented.
- They are often .html files, with HTML  code describing the layout of the web page, but it can also be in other file formats to present other results.

- Django uses standard HTML to describe the layout, but uses Django tags to add logic.
```Django
<h1>My Homepage </h1>
<p>My name is {{ firstname }}.</p>
```
### URLs
- Django provides a way to navigate around pages in a website.
- When a usesr requests a URL, Django decides which `view` it will send it to, done in a file called `urls.py`

### How Django works- 
- When the browser requests the URL, this is basically what happens:
1. Django receives the URL, checks the `urls.py` file, and calls the view that matched the URL.
2. The view, located in `views.py`, checks for relevant models.
3. The models are imported fron the `models.py` file.
4. The view then sends the data to a specified template in the `template` folder.
5. The template contains HTML and Django tags, and with the data it returns finished HTML content back to the browser.

## Django Getting Started
### Django Requires Python 
To check if your system has Python installed, run this command in the terminal:
```python
python3 --version
```
or
```python
python --version
```

### PIP
To install Django, you must use a package manager like PIP.
```python
pip --version
```


## Creating Virtual Environment
### Virtual Environment
It is suugested to have a dedicated virtual environment for each project, and one way to manae a virtual environment is venv which is included in Python.

1. Create the environment
 Unix/macOS
```py
python -m venv myworld
```
This will set a virtual environment, and create a folder named "myworld".
2.  ACtivate the environment
```py
source myworld/bin/activate
```
### `NOTE:` You must activate the environment every time you open the command prompt to work on yourproject.

## Install Django
Django is installed using pip, with this command:
```py
(myworld) ... $ python -m pip install Django
```
