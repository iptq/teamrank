FROM python:3.6-slim

# working directory
RUN mkdir /app
WORKDIR /app

# gunicorn
RUN pip install gunicorn

# dependencies
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

# main app now
COPY . /app/
EXPOSE 5000

ENTRYPOINT ["/usr/local/bin/gunicorn", "-b", "0.0.0.0:5000", "teamrank.create_app()"]