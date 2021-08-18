# pull the official docker image
FROM python:3.8.3-slim

# set work directory
WORKDIR /app

# set env variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# copy project
COPY . .

# install dependencies
RUN pip install -r requirements.txt

# Run command
CMD ["python", "-m", "spacy download en_core_web_sm"]
CMD ["uvicorn", "app.main:app"]