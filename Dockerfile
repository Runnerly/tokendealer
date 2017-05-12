FROM python:3.6

COPY . /app
RUN pip install -r /app/requirements.txt
RUN pip install /app/

EXPOSE 5000
CMD runnerly-tokendealer
