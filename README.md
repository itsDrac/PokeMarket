# PokeMarket
This is an fullstack e-commerce web application where in you can buy Pokemons with real money. This is build using flask and htmx.

---
[This](https://github.com/users/itsDrac/projects/1) is the github project page for PokeMarket application
[This](https://drawsql.app/teams/freelancer-84/diagrams/pokemarket) is the link to database diagram (in this project I am using drawsql.app)

## Setup
To setup the application locally you can clone(download) this repo and have a `.env` file similar to `.env.sample`, and install all the requirements with

```shell
pip install -r requirements.txt
```

With all the requirements installed before running its good to run pytest to check if all the tests are passing. Once done, use below command to run the application

```shell
flask run
```

To run in debug mode please set `DEBUG=1` in `.flaskenv` file.
