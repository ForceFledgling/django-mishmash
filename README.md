# 🙉 What's all the CUST?

Cross-platform users script toolkit - this is CMS, containing scripts, developed over time, to automation of routine tasks, assembled on:

* Infrastructure: Docker-compose
* Web servers: Nginx
* Web apps: Django Channels (JSON RPC API)
* Frontend: HTML5 Bootstrap, jQuery
* Databases: PostgreSQL, Redis

The GitHub repository houses the components needed to build cust as a container. Images are will be built regularly using the code in that repository and are pushed to Docker Hub.

## ⚡ Fast implementation

**Step 1:** If not installed, download and install docker and docker-compose:
* Get Docker - https://docs.docker.com/get-docker/ (see the **Dependencies** section)

**Step 2:** Cloning the project:
```bash
    git clone -b release https://github.com/pvenv/cust-docker.git
```

**Step 3:** Creating **.env** files in cust-docker folder (see the **Env examples** section):

**Step 4:** Running and usage the project:
```bash
    cd cust-docker
    chmod +x docker/web/entrypoint.sh
    docker-compose up -d
```

The whole application will be available after a few minutes. Open the URL http://127.0.0.1/ in a web-browser.
The default credentials are:
* login: admin
* password: admin


## 🎉 Env examples

Example env/cust.env file:
```bash
    #BASE
    VERSION='x.x.x'
    DEBUG='True'
    LOCAL_IP='185.105.89.18'
    SECRET_KEY='dm42@3kbj10b2gse&h%o)1ef&rn42k)e_a'
    TIME_ZONE='Asia/Yekaterinburg'

    #DATABASE
    DB_HOST='db'
    DB_NAME='web'
    DB_USER='user_web'
    DB_PASSWORD='custDB_P@ssw0rd'

    #SEUPERUSER SETTINGS
    DJANGO_SUPERUSER_EMAIL='admin@example.com'
    DJANGO_SUPERUSER_USERNAME='admin'
    DJANGO_SUPERUSER_PASSWORD='admin'
```

Example env/postgres.env file:
```bash
    POSTGRES_DB='db_name'
    POSTGRES_USER='db_username'
    POSTGRES_PASSWORD='db_passwrod'
```

## Dependencies

This project relies only on *Docker* and *docker-compose* meeting these requirements:

* The *Docker version* must be at least `19.03`.
* The *docker-compose version* must be at least `1.28.0`.

To check the version installed on your system run `docker --version` and `docker-compose --version`.

## Updating
...

## Recreating containers with data removal
```bash
    docker-compose up --build --remove-orphans
```

## Demo
In the future, the site will be fully open for viewing, at the link http://custproject.ru

## Screenshots

### Wiki page
![image](https://user-images.githubusercontent.com/92352077/168686542-ad378adb-b563-4750-b244-fe8568c8b27d.png)

## Contributing

If you are looking to contribute to this project, first of all, thank you!


<br />
<br />