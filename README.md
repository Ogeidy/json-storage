# json-storage
Test project of web service using Flask and PostgreSQL


## Some useful commands

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


Create PostgreSQL docker container:
~~~
docker run -d --name dbTest \
    -v /home/diego/Development/postgres/dbTest:/var/lib/postgresql/data \
    --restart=always \
    -e POSTGRES_PASSWORD=test \
    -p 5432:5432 \
    postgres
~~~