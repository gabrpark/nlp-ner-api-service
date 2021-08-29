# Named Entity Recognition Service

## Summary

**[Named-Entity Recognition (NER)](https://en.wikipedia.org/wiki/Named-entity_recognition)** is a subfield of Natural Language Processing (NLP) to classify named entities in text. Our goal is to build a web-based API-service to provide text analysis with NER.

#### Directory Structure
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

#### Request Flow

Web-Browser -> Waved -> Wave app -> API service

## Running this App Locally

#### With Docker

To start the service, run the following command at the root directory where `docker-compose.yml` is located:
```
docker-compose up
```

To stop the service, execute:
```
docker-compose down
```

#### Without Docker

1. Follow the installation step for [H2O Wave](https://wave.h2o.ai/docs/installation) and for [FastAPI](https://fastapi.tiangolo.com/). Also, install [SpaCy](https://spacy.io/usage) and [Requests](https://www.geeksforgeeks.org/how-to-install-requests-in-python-for-windows-linux-mac/) python packages. (I recommend to use a virtual environment such as **venv** or **conda** for this test.)

2. Open up another shell. Go to `/api_service/app/`, and execute the following command:
```
uvicorn main:app --reload
```

3. This is the command to start the Wave server as shown in the step.
```
./waved
```

4. Open up a new shell. Move to `/ui/wave_app/`, and run `wave_app.py` with `wave run` command as follows:
```
wave run wave_app.py
```

5. On your preferred web browser, go to this URL: `localhost:10101/wave_app`. A text box with a submit button will display on the page. To stop the service, press `Command+C` from each shell (`Ctrl+C` for **Windows** users).

## Technologies

#### FastAPI

The Service is built with Fast API. This API-Service receives the user input by the UI and any other http client to run **NER** on a given text.

#### H2O Wave

H2O Wave is used as front-end stack.

The UI contains:

- A submit page with text box to enter the text.
- A result page to display the **NER** analysis for the text.

#### Docker

Dockerfiles are created to build docker images for the API-Service and the UI.

#### Docker Compose

A docker-compose file, `docker-compose.yml`, is created to start all the required containers.

<!-- #### Test / Demo

- Use the `docker-compose up` command to start all the involved Services![](Aspose.Words.0ea28836-a8cc-4dea-8f6c-cb5332e3b97a.007.png)
- Connect UI to Web-Browser
- Enter text
- Submit text to process **NER**
- Display results -->

## Issues
- `wave run wave_app.py` fails with Docker Compose

## System Requirements
- [Docker Engine](https://docs.docker.com/engine/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Python 3.8.3](https://www.python.org/downloads/release/python-383/)
- [spaCy 3.1.1](https://pypi.org/project/spacy/)
- [Fast API: Http Service Framework](https://fastapi.tiangolo.com/)
- [H2o Wave: UI Framework](https://wave.h2o.ai/)
