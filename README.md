# anaconda-challenge
Anaconda coding challenge

This is solution of Adam Stibal for the Anaconda coding challenge [description here](https://docs.google.com/document/d/19S6RcSmjbGSwZKDz1kQhNMVs1xLPnNmf3X2qhrOkk5E/edit#heading=h.qvci9sf9j9ne)

The goal is to implement Rock Paper Scissors game as a web application. Here I will put most of my concentration on backend, since I'm applying for a Python backend position. I will create the solution as an API using FastAPI, sqlalchemy on sqlite. The motivation for that is simple: FastAPI is without doubt the best web framework with especially practical shortcuts to create well documented APIs. Swagger and OpenAPI documentation comes with FastAPI by default, which let's BE developers to perform basic manual testing of the API and FE developers can profit from the openapi.json file provided to create their JS models automatically from the provided definitions.
Sqlalchemy with sqlite will be needed to provide the persistence layer for the app. Sqlite is a good enough database for such PoC. For any production software some other much more capable database engine would be reqiured.
