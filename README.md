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

### Tested Operative System:

- Windows 10: Error in use of python OS library.
- All linux-based os: OK

### Steps

1. Clone repository.
2. Create and activate a virtual environment.
3. Start redis server or connect to one and check redis server configuration on ```.env``` (This file is created as a copy of ```.env.example```):

    ```REDIS_HOST=localhost```

4. Basic django configurations:

    ```pip3 install -r requirements.txt```
    
    ```python manage.py migrate```
    
    ```python manage.py collectstatic```

5. Start worker management:

    ```python manage.py rqworker default```
    
6. Start django server:
    
    ```python manage.py runserver```
    
## Docker-Composer

### Tested Operative System:

- Windows 10: OK
- All linux-based os: OK

### Step

1. Check redis server configuration on ```.env``` (This file is created as a copy of ```.env.example```):

    ```REDIS_HOST=redis```

2. Execute Docker Compose:
    
    ```docker-compose up```

# Help?

Please, contact me to: dapalominop@gmail.com