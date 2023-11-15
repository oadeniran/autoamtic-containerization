FROM python:3.9

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install --no-cache -r requirements.txt

EXPOSE 5000

COPY . .

CMD [ "python", "index.py" ]