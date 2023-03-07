# Pokédex Streamlit Webapp
<br>

## Overview
  This is a Pokédex webapp made in Streamlit, with a wealth of features which outshines any of the in-game Pokédexes in any of the Pokémon games.
  
  This webapp was my introduction to programming and python. I wrote the code in my first semester of college.
  You can access the cloud version of the webapp through this link:
  
  
  The webapp mixes english and the portuguese language, because the data I used was ripped from the game in english, but the project was shown to a brazilian audience.
  
  If the link stops working or if you want to access a local version of the app, you can do so by going to the "Local Webapp Setup" section of the README.
  
  Uploading the project to GitHub was my introduction to Git and GitHub.
  
 ## Functionalities
 * All of the data is adjusted to each generation, so if you change the generation, the data of the Pokémon changes to reflect what changes in each game.
 * Has all Pokémon up to Generation 8, which was the newest generation at the time.
 * Has in-game ripped pokédex data, e.g.: Species, Weight, Height, Ability, Male/Female ratio, ect...
 * Has some battle data, e.g.: Weakness chart, Base Stats, Growth rate, Catch Rate, ect...
 * Has egg data, e.g: Egg Cycles, Base Happiness, Egg Group, ect...
 * All possible sprites are displayed per generation, with front and back sprites, each game in said gen, sprites that change with gender, shiny sprites, models, ect...
 * Many different artworks can be displayed per Pokémon.
 * Has a hidden data toggle for more experienced Pokémon players, which display things such as hidden abilities, names of the pokemon in different languages.
 * Can show every Pokémons cries, and has toggles for Pokémon with more than one, such as Pikachu.
 * Has a list of every learnable move up to generation 8.
 * Has every Pokédex entry for each Pokémon.
 * Displayes sprite animations from gen 5.
 <br>
 
## Local Webapp Setup
* Use the Git Clone command, if you don't know how, refer to this tutorial by GitKraken. Make sure you have all of the libraries needed to run. You can double check them in requirments.

https://www.youtube.com/watch?v=aHMPn57ZmJo

* Run the "main.py" file.
* The terminal will give you a command. (it should look like "streamlit run <directory>") Copy and Paste it into your CMD and run it.
* The app should display on your local host.
<br>

## Addendum
* If you are running the cloud version of the webapp, it initially will take a while to load all of the files. This may cause certain images and sprites to not load immediatly. This problem should go away after normal usage of the app.
* The app doesn't display the moveset for each Pokémon due to me not knowing how to implement this feature when the app was developed.
