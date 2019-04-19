FROM python:3.7
ADD . /usr/src/app
WORKDIR /usr/src/app
EXPOSE 4000
RUN pip install -r requirements.txt
ENTRYPOINT ["python","rest-api.py"]