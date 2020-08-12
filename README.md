# Multiroom-chatbot

Multiroom chatbot in Django with RQ.

## Requeriments
- python==3.6.8
- django==2.2
- djangorestframework==3.9.3
- redis==3.2.1
- django-rq==2.0

(*) For a complete revision, please check *requeriments.txt* file.


# How to setup

This guide is for setting up development instances.

## Virtualenv

### Steps

1. Clone repository.
2. Create and activate a virtual environment.

3. Basic django configurations:

    ```pip3 install -r requirements.txt```
    
    ```python manage.py migrate```
    
    ```python manage.py collectstatic```

4. Start redis server or connect to one.

5. Start worker management:

    ```python manage.py rqworker default```
    
6. Start django server:
    
    ```python manage.py runserver```
    
## Docker-Composer

### Step

    asdas
    asdsa

#Help?
Please, contact me to: dapalominop@gmail.com