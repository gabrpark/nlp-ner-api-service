**Build Named Entity Recognition Service with SpaCy and Python**

***Summary***

**[Named-Entity Recognition (NER)](https://en.wikipedia.org/wiki/Named-entity_recognition)** is a subfield of Natural Language Processing (NLP) to classify named entities in text. Our goal is to build a web-based API-service to provide text analysis with NER.

**Directory Structure**
```
├── README.md
├── api_service
│   ├── Dockerfile
│   ├── app
│   │   └── main.py
│   └── requirements.txt
├── docker-compose.yml
└── ui
    ├── Dockerfile
    └── wave_app
        ├── Dockerfile
        ├── requirements.txt
        └── wave_app.py
```

**Request Flow**

Web-Browser -> Waved -> Wave app -> API service

**API-Service**

The Service is built with Fast API. This API-Service receives the user input by the UI and any other http client to run **NER** on a given text.

`main.py` can be found at `api_service` -> `app` directory.

```
uvicorn app.main:app
```

**UI/Front-End**

H2O Wave is used as front-end stack.

The UI contains:

- A submit page with text box to enter the text.
- A result page to display the **NER** analysis for the text

Start the waved server:
```
./waved
```

Start the UI:
```
wave run wave_app.py
```

**Docker**

Dockerfiles are created to build docker images for the API-Service and the UI.

**Docker Compose**

A docker-compose file, `docker-compose.yml`, is created to start all the required containers.

**Test / Demo**

- Use the `docker-compose up` command to start all the involved Services![](Aspose.Words.0ea28836-a8cc-4dea-8f6c-cb5332e3b97a.007.png)
- Connect UI to Web-Browser
- Enter text
- Submit text to process **NER**
- Display results

***Issues***
- `RUN pip install spacy` fails in Dockerfile
- `wave run wave_app.py` fails with Docker Compose

**Prerequisites**
- [Docker Engine](https://docs.docker.com/engine/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Python 3.8.3](https://www.python.org/downloads/release/python-383/)
- [spaCy v3.1.1](https://pypi.org/project/spacy/)
- [Fast API: Http Service Framework](https://fastapi.tiangolo.com/)
- [H2o Wave: UI Framework](https://wave.h2o.ai/)
