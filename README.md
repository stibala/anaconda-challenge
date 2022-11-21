# anaconda-challenge
Anaconda coding challenge

This is solution of Adam Stibal for the Anaconda coding challenge [description here](https://docs.google.com/document/d/19S6RcSmjbGSwZKDz1kQhNMVs1xLPnNmf3X2qhrOkk5E/edit#heading=h.qvci9sf9j9ne)

The goal is to implement Rock Paper Scissors game as a web application. Here I will put most of my concentration on backend, since I'm applying for a Python backend position. I will create the solution as an API using FastAPI, sqlalchemy on sqlite. The motivation for that is simple: FastAPI is without doubt the best web framework with especially practical shortcuts to create well documented APIs. Swagger and OpenAPI documentation comes with FastAPI by default, which let's BE developers to perform basic manual testing of the API and FE developers can profit from the openapi.json file provided to create their JS models automatically from the provided definitions.
Sqlalchemy with sqlite will be needed to provide the persistence layer for the app. Sqlite is a good enough database for such PoC. For any production software some other much more capable database engine would be reqiured.

## installation
The project uses poetry for dependency management. First, clone the repository:
```bash
git clone https://github.com/stibala/anaconda-challenge.git
cd anaconda-challenge
```

then install requirements:
```bash
poetry install
```

The next step is to use Alembic to setup the database:
```bash
alembic upgrade head
```

The API can be started using uvicorn:
```bash
uvicorn main:app --reload 
```
This will start running the app on localhost port 8000. The Swagger documentation can be viewed at http://localhost:8000/docs

## description
This app is a basic implementation of Rock Paper Scissors game. The intended workflow consists of following steps:
1. Create at least 2 users via POST /users/signin. In order to support computer as an opponent, a user named as `computer_name` in .env settings has to be added.
1. The user that wants to create a new game has to authorize via the Authorize button with own credentials. This will create an JWT token for the user which has expiration duration of 30 minutes.
1. Authorized user can then create a game via POST /game providing `other_user_name` in the payload or leaving empty payload to let `computer` be the opponent.
1. After game has been initialized with 2 users, a new `turn` can be generated via POST /game/{game_id}/turn, where game id has to be provided. Depending on whether the opponent is computer or not, a `throw` will be automatically generated with random value from rock, paper or scissors. This will be displayed in the response payload.
1. A user can throw, i.e. select own choice from rock, paper or scissors for a turn via POST /throw with payload containing turn_id and value. If the user wishes a random value to be generated for the throw, the value may be omitted. Depending on whether the opponent is computer or not, the turn may be finished and winner will be determined.
1. After a turn has been finished, the winner can be determined by GET /turn/{turn_id}. Response body example:
```json
{
  "game_id": 2,
  "id": 2,
  "winner": "adam",
  "finished": true,
  "throws": [
    {
      "turn_id": 2,
      "value": "rock",
      "username": "computer",
      "id": 3
    },
    {
      "turn_id": 2,
      "value": "paper",
      "username": "adam",
      "id": 5
    }
  ]
}
```

One game can have any number of turns. Any user can generate any number of games, as long the opponent user name exists in the database.
There is a tiny test suite to demonstrate testing approach. Only three test cases are implemented to test creating, getting and deleting a user using pytest. This isn't ment to be complete, in real life this would be absolutely insufficient.

## further development
This basic API is far from complete. Rather it's a PoC backend API for allowing Frontend to build a UI application. There are several issues with this API draft. Mainly
1. incomplete CRUD endpoints for user, game, turn and throw. For instance there is no way to change user email address. As the time limit for this challenge was very tight (3 hours), there wasn't enough time to implement more complete solution.
1. there is no invitation mechanism in order to inform the opponent about the fact a new game which requires his/her participation has been created.
1. security issues: every user can display every game or turn. In real life this would be inacceptable.
1. endpoint GET /game/{game_id} returns all turn ids for a specific game, which may get arbitrarily big. Only acceptable for this PoC. In real life, there would be needed to create another endpoint which lists all turns for a specific game with pagination to allow infinite scrolling or similar UI approach.
1. database architecture is not particularly elegant. Especially the fact that the game DB model saves user names instead of IDs. The same applies to throw. For the sake of keeping this PoC sane, the user names are directly stored with the game, instead of creating a many to many relationship to user table.
1. almost all logic like validating existence of the DB item, creating randoms, validating input data or determining winners is implemented on the router level or DB model level. This isn't particularly elegant and correct. Another level of separation would be needed for real life implementation.
1. unit-testing of whole scenarios would be needed

## other issues
No UI has been even tried to create for this API since the time limit was too tight. Even though I tried to reduce the functionality to bare minimum to fit into the time limit, I didn't manage it under 3 hours. I spend some time by setting up the JWT authentication, which I believe is necessary. Although the JWT implementation is mostly copied from the FastAPI documentation, I had to invest some time to bind it to my models and database. Furthermore I had to resolve an issue with Alembic, which wasn't initially generating automatical DB migrations. I surely spent an hour by preparing the design and writing this documentation. I didn't want to present an incomplete app, so I finished the basic functionality. I sincerely guess the time spent on the whole app around 6-7 hours. Within 3 hours, I would have hade authentication layer, all database models, documentation and maybe first endpoints for creating a game.

## summary
I really enjoyed working on this task. Even the base game algorithm is absolutely simple (see function winner in app/db_models/turn), the whole API did take substantially more time to finish. On the other hand, I can present an API with some cool features like authomatic OpenAPI documentation, JWT authentication or API design that enables using WebSocketAPI in order to allow both players to play simultaneously the turn under their accounts.

Looking forward to discussing this solution in the technical round!


