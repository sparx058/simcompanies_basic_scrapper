# Sim Companies Scrapper
Pretty basic and bare bones Sim Companies Player Info Scrapper.
Currently, it has following features:
- Returns Name, ID, Level, Rank, Date & Time Joined
- Saves this data into a `.csv`[comma seperated] file

## Usage
In the file **sim_companies_scrapper_main.py :** 

`65. s_id = 1032750`

`66. e_id = 1032760`

- Change variables `s_id`  [starting id] & `e_id` [ending id] , to start search for player ID's
-If you want to just look for one player ID, then put `s_id` & `e_id` as `player_id-1` & `player_id+1` respectively.

Eg, I want to look up ID:1004078 the my lines will look like

`65. s_id = 1004077`

`66. e_id = 1004078`

-  You can find you ID by going to [My ID](https://www.simcompanies.com/api/v2/players/me/ "My ID"), if you have an account already.

The default program runs for  range `[1032750-1032760]`.

Thats it for  my second ever half-decent python program.


