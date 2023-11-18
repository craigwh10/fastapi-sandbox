FROM python:3.8-slim-buster

WORKDIR /src

# Mount index.py as a volume in run.
COPY requirements.txt ./

RUN pip3 install -r requirements.txt

# Expose port
EXPOSE 3000

# Run flask --app index run
CMD [ "hupper", "-m", "index"]