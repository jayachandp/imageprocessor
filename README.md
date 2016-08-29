## Steps to run the application locally.

1. Install virtualenvwrapper (First time only)  
    `pip install virtualenvwrapper`

2. Create a virtualenv  
    `mkvirtualenv imageprocessor`.  
   If the virtualenv already exists, just activate it  
    `workon imageprocessor`

3. Install the requirements  
    `pip install -r requirements.txt`

4. Migrate the application  
    `python manage.py migrate`

5. Run the appliation  
    `python manage.py runserver`

6. For console  
    `python manage.py shell_plus`
