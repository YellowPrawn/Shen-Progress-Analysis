# Teemo Ultimate Progress
The objective of this project is determining if my usage of Teemo's (League of Legends) ultimate ability (shrooms) usage has increased in effectiveness. The player data is obtained through the Riot API and the RiotWatcher library. 

From my basic exploration of the match timeline API, only damage which results in a kill and "ward" placement/destruction is recorded. Since Teemo's shrooms count as wards, it may be adequate to compare the number of shrooms placed, destroyed, and the ones which participated in a kill in determining their effectiveness in-game.

With the public API key, we are only able to access the past 100 matches played by the given player. Therefore, this analysis will have dynamic results depending on the past 100 matches of League Of Legends the player has played. Therefore, results may sometimes be unreproducible due to the ever changing nature of a player's match history.

### Contributors: Damien Fung

# Dependencies
- numpy=1.22.2
- pandas=1.4.1
- pytest=6.2.5
- riotwatcher=3.2.3

# Usage
To use this project, first ensure Git is installed in your system. Then, clone this project by pasting one of the following commands into your system terminal

- HTTPS clone:
```
git clone https://github.com/YellowPrawn/Teemo-Trade-Progress.git
```
OR
- a SSH clone:
```
git clone @github.com:YellowPrawn/Teemo-Trade-Progress.git
```

The project dependencies can be accessed quickly through the `environment.yml` file using conda. To do this, ensure conda is installed, navigate to the root directory, then type the following in your terminal
``` 
conda env create --file environment.yml
```

In order to run the scripts in this project, you will need a Riot API key. You can generate a developer key through the [Riot Developer Portal](https://developer.riotgames.com/).

After obtaining an API key, place it in the `api_key.txt` file in the root directory. 

To recreate the analysis and findings, run the command
```
make
```
into the terminal to run the Makefile script.

To clean up the directory, use the command
```
make clean
```

To run the test scripts. To perform the tests, navigate to the root directory and enter 
``` 
pytest
``` 
into the terminal


# Disclaimer
Teemo Ultimate Progress isn't endorsed by Riot Games and doesn't reflect the views or opinions of Riot Games or anyone officially involved in producing or managing Riot Games properties. Riot Games, and all associated properties are trademarks or registered trademarks of Riot Games, Inc.
