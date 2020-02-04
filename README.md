# Poker

## Set up

There is a `Dockerfile` that will make the setup and interaction with the app
easier. To be able to do so, please start with:

```
docker build -t py_ker .
```

## Running it

### Default

By default, it will execute tests. Please use:

```
docker run py_ker
```

### Running game with default cards

Script will allow playing a game with a default set of cards.

To do so, please run:

```sh
docker run py_ker /bin/sh -c "python main.py"
```

### Running game with custom cards

Alternatively, it is possible to play the game with a custom set of cards.

In order to do so, provide a string with card representations as a second
argument, like:

```sh
docker run py_ker /bin/sh -c "python main.py 'TH JH QH KH AH, 5S 7C KC KH KD'"
```
