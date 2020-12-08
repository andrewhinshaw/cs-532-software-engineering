# Icetrack

Icetrack is an Python Django-based automated tracking system for Tom and Adam’s Ice Cream Company. The web application, referred to as ICETRACK, supports the following business functional areas: order entry, inventory management, shipment tracking, trouble ticket management.

## Quickstart

Requirements: Must have Python installed

Clone the repo into a local directory or download and use the included filesystem.
```
git clone https://github.com/CS532-Ice-cream/icetrack.git
```

Change directories into the project directory
```
cd <project-directory>
```

Create a new virtual environment and install django
```
pipenv install django~=3.1.0
```

Activate the virtual environment
```
pipenv shell
```

Run the Django application
```
python manage.py runserver
```

In your browser, navigate to http://127.0.0.1:8000/
