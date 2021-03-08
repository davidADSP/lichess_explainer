# lichess_explainer
Suggests ways you can improve you chess through analysis of your lichess game history


# Setup

download the pgn of your games from lichess and place the file in the ```data``` folder, naming the file the same as your username
e.g. datashrimp.pgn

Download stockfish into the root directory (e.g. the stockfish version I reference in the code is at ```./stockfish/Mac/stockfish-10-bmi2```)

# Run

Currently in notebooks.

Train on your own data by running the cells in train.ipynb
This outputs pkl files to the store

Analyse your openings in analyse.ipynb