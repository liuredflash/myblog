FROM python:latest

WORKDIR /usr/local
RUN mkdir ./my_web_server
ADD Demo ./my_web_server/
ADD requirements.txt ./my_web_server/

WORKDIR my_web_server/
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "demo.wsgi", "-b", "0.0.0.0:8000", "&"]
