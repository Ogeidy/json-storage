FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

VOLUME ./instance

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["-m", "json_storage"]
