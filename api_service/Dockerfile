# pull the official docker image
FROM python

# set work directory
WORKDIR /app

# copy project
COPY . .

# install dependencies
RUN pip install -r requirements.txt
RUN pip install -U pip setuptools wheel
RUN pip install -U spacy==3.1.1
RUN python -m spacy download en_core_web_sm

# Run command
CMD ["uvicorn", "app.main:app", "--reload"]