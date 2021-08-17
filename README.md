**Build Service and UI to Showcase Named Entity Recognition *Technologies, Languages***

- Definition [Named Entity Recognition/NER](https://en.wikipedia.org/wiki/Named-entity_recognition)![](Aspose.Words.0ea28836-a8cc-4dea-8f6c-cb5332e3b97a.001.png)
- [Docker Engine](https://docs.docker.com/engine/)![](Aspose.Words.0ea28836-a8cc-4dea-8f6c-cb5332e3b97a.002.png)
- [Docker Compose](https://docs.docker.com/compose/)![](Aspose.Words.0ea28836-a8cc-4dea-8f6c-cb5332e3b97a.003.png)
- [Python 3.x](https://www.python.org/downloads/)![](Aspose.Words.0ea28836-a8cc-4dea-8f6c-cb5332e3b97a.004.png)
- [spaCy v3.1](https://spacy.io/)![](Aspose.Words.0ea28836-a8cc-4dea-8f6c-cb5332e3b97a.005.png)
- [Fast API: Http Service Framework](https://fastapi.tiangolo.com/)![](Aspose.Words.0ea28836-a8cc-4dea-8f6c-cb5332e3b97a.006.png)
- [H2o Wave: UI Framework](https://wave.h2o.ai/)

***Overview***

To showcase and test **NER** we will build a Service and a UI and bundle everything to be executed with Docker Compose.

All the necessary code will be written in Python.

***API-Service***

The Service will be built using Fast API. The Service will offer an HTTP based API. This API can be used by the UI and any other http client to run **NER** on a given text.

The Service will be using spaCy for **NER**.

***UI***

We will build a simple UI using Wave. Wave consists of a UI-daemon (Waved) and the Wave application-specific service. The UI will interact with the API-Service over HTTP.

The UI should at minimum contain:

- A text entry field to enter the text to be analyzed.
- A button to initiate the request to the Service. The request will pass the text entered to the Service using HTTP and wait for the response.
- A result-output to show the result of the **NER** for the given text

***Docker Compose***

As an execution platform for the API-Service and the UI services we will be using Docker Engine and Docker Compose.

Each component, API-Service, and UI (Waved and Wave application) will individually be built in to a Docker Image. To build the Docker Image for the API- Service and the UI a Dockerfile has to be written. Below you will find the Dockerfile for Waved.

To start all the Services we use Docker Compose. A docker-compose file has to be written to have Docker Compose start all the needed Services.

***Test / Demo***

- Use the  docker-compose up command to start all the involved Services![](Aspose.Words.0ea28836-a8cc-4dea-8f6c-cb5332e3b97a.007.png)
- Use Web-Browser to connect to UI
- Enter text in UI
- Submit text to process **NER**
- Result will be shown in UI

***Request Flow***

Web-Browser -> Waved -> your Wave app -> your API service

***Dockerfile Waved***

```FROM ubuntu:18.04![](Aspose.Words.0ea28836-a8cc-4dea-8f6c-cb5332e3b97a.008.png)

RUN apt-get update

RUN apt-get -y install wget

RUN wget https://github.com/h2oai/wave/releases/download/v0.16.0/wave-0.16.0- linux-amd64.tar.gz

RUN tar -xvf wave-0.16.0-linux-amd64.tar.gz && mv wave-0.16.0-linux- amd64 /wave && chmod +x /wave/waved

WORKDIR /wave

EXPOSE 10101/tcp

ENTRYPOINT ["./waved"]```
