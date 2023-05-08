FROM  python:3.9

ENV PYTHONUNBUFFERED=1

WORKDIR /dockerapp

COPY requirements.txt . 

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver"]