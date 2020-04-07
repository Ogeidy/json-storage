# json-storage
Test project of web service using Flask and PostgreSQL


## API reference

Add JSON
~~~
curl -s -H "Content-Type: application/json" -d '{"one":5, "two":"second"}' http://127.0.0.1:5000/api/json
~~~

Get all JSONs
~~~
curl -s  http://127.0.0.1:5000/api/json
~~~

Get particular JSON
~~~
curl -s http://127.0.0.1:5000/api/json/1
~~~

Delete JSON
~~~
curl -s -X "DELETE" http://127.0.0.1:5000/api/json/2
~~~

Change already existing JSON
~~~
curl -s -H "Content-Type: application/json" -X "PUT" -d '{"new":5, "key":"second"}' http://127.0.0.1:5000/api/json/10
~~~


## Deploying manual

Create PostgreSQL container:
~~~
docker run -d --name dbTest \
    -v $PWD/postgres/dbTest:/var/lib/postgresql/data \
    --restart=always \
    -e POSTGRES_PASSWORD=test \
    -p 5432:5432 \
    postgres
~~~

Create database:
~~~
docker exec -ti dbTest psql -U postgres -c 'CREATE DATABASE test'
~~~

Build json-storage image:
~~~
docker build . -t json-storage
~~~

Create json-storage container:
~~~
docker run -d --name jsonStorage \
     --link dbTest:db \
     -p 5000:5000 \
     -v $PWD/instance:/usr/src/app/instance \
     json-storage
~~~
