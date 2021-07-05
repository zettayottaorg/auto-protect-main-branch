FROM python:3
WORKDIR /app
ENV FLASK_APP=listener.py

COPY listener.py .
COPY configs .

RUN pip install --no-cache-dir Flask
RUN pip install --no-cache-dir requests

RUN ls 
expose 5000
ENTRYPOINT flask run --host=0.0.0.0