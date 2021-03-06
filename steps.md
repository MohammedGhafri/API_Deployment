# class 34 Authentication & Production Server

## First Part

1. In terminal :
    - poetry add django-cors-headers
    - poetry add django-environ
    - poetry add psycopg2-binary
    - poetry add psycopg2



2. project folder (Not root):

    - create sample.env (This step is optional, for educational purposes)

        - ```DEBUG=on
            SECRET_KEY=put-real-secret-key-here
            DATABASE_NAME=postgres
            DATABASE_USER=postgres
            DATABASE_PASSWORD=put-real-db-password-here
            DATABASE_HOST=db
            DATABASE_PORT=5432
            ALLOWED_HOSTS=localhost,127.0.0.1,172.16.0.163
            ```
    
    - Create .env

        - ```DEBUG=on
            SECRET_KEY=put-real-secret-key-here
            DATABASE_NAME=postgres
            DATABASE_USER=postgres
            DATABASE_PASSWORD=put-real-db-password-here
            DATABASE_HOST=db
            DATABASE_PORT=5432
            ALLOWED_HOSTS=localhost,127.0.0.1,172.16.0.163
            ```
        - Modify the some fields such as DEBUG = off, database password,secretkey ..

3. In project.settings : 
    - import
    - Add :
        - ```
            env = environ.Env(
            # DEBUG is Flase by default
            DEBUG = (bool, False)
            )
         ```
        - `environ.Env.read_env()`
        - 
    
    - Move the value of the secret key to .env and make the SECRET_KEY = `env.str('SECRET_KEY')`
    - DEBUG = `env.bool('DEBUG')`
    - ALLOWED_HOSTS= `tuple(env.list('ALLOWED_HOSTS'))`
    - DATABASE = 
    ```
    - DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('DATABASE_NAME'),
        'USER': env.str('DATABASE_USER'),
        'PASSWORD': env.str('DATABASE_PASSWORD'),
        'HOST': env.str('DATABASE_HOST'),
        'PORT': env.str('DATABASE_PORT')
    }
    }
    ```

4. In Dockerfile:
    -after `ports` add :
    ```
                        -     depends_on:
                                - db
                            db:
                                image: postgres:11
                                environment:
                                    - "POSTGRES_HOST_AUTH_METHOD=trust"
    ```
    
5. In terminal :
    - `docker-compose up -d`
    - `docker-compose exec web python manage.py migrate`
    - to check if the server is running use `docker-compose ps` you must see somthing like :
    ```
        Name                      Command               State           Ports
    --------------------------------------------------------------------------------------
    api_deployment_db_1   docker-entrypoint.sh postgres    Up      5432/tcp

    api_deployment_web_1   gunicorn drf_auth.wsgi:app ...   Up      0.0.0.0:8000->8000/tcp

    ```

    if You see didnt see the server you need to run `docker-compose up`
    - `docker-compose down`
    
    - `docker-compose up --build -d` or without `-d`

6. In main folder(root): 
    - Create folder "static:

7. In terminal :
    - `docker-compose exec web python manage.py collectstatic`
    - `docker-compose exec web python manage.py createsuperuser` 

8. In project.settings 
    -In "INSTALLED_APP", after 'rest_framework' add "'corsheaders',"
    -In "MIDDLEWARE" , at the beginning add "'corsheaders.middleware.CorsMiddleware',"
    - At the bottom 

                ```
                CORS_ORIGIN_WHITELIST = [
                'http://localhost:3000',
                ]

                ```
9. Don't forget to add .gittgnore as I did

# Comming soon

## Deploy on heroku 

1. Make sure you have heroku in your machine, if Not use this code `curl https://cli-assets.heroku.com/install.sh | sh` in your Terminal.
2. In Terminal :
    - `heroku create <name  your app >` make sure you didn't exceeded the allowed free apps, which is just 5
    - ِA link will show up, This is your domain
3. In root : 
    - create file "heroku.yml"
    - inside this file :

        ```
        build:
            docker:
            web: Dockerfile
            
        release:
            command:
            - mkdir -p static
            - python manage.py collectstatic --noiput
            - ./deployment-tasks.sh
            image: web
        run:
            web: gunicorn drf_auth.wsgi
        
        ```

4. In terminal, Make sure you are project is connected to githup :
    - `heroku git:remote -a <name of app from step 2>
    - `git remote -v` You must see heroku directory
    - add
    - commit
    - `heroku stack:set container`
    - git push heroku <branch>
