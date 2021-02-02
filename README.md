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

## Update 1

### Speed-up

If you ever used the original upload, you would remember how slow it was

Well, now its much faster. Still not fast but very much better than before.

Here's a benchmark to easily grasp the difference:

| Players | Time(s) | %CPU* | %RAM* | O/U** |
| ----- | ----- | ----- | ----- | ------ |
| 5 |8.553489 | 14.0| 86.8| o |
| 15 |34.103951 | 12.5 | 88.1 | o |
| 50 | 98.294622 | 12.7 | 87.6 | o |
|50|182.258425|17.5|88.6|o
|10|30.753759|12.9|88.1|o
|10|34.316963|12.3|84.6|o
|10|45.221586|12.0|84.6|o
|10|37.671155|12.5|85.4|o
|10|29.757702|12.5|73.8|u
|15|47.862738|13.3|75.7|u
|15|17.367993|12.4|75.7|u
|50|46.582664|13.3|75.1|u
|50|48.325764|11.1|74.6|u
|500|515.961511|15.2|74.4|u

*percentage utilization

**o for Original , u for Update 1

Here's some graphs to understand if you're even more retarded than me

![contact me if this goes down](https://i.imgur.com/SrAJ0Un.png) ![ontact me if this goes down](https://i.imgur.com/WHwzLo9.png) 
