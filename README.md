# Warpin' Walter

<img src="/screenshots/menu.gif" width="320" height="240" />    <img src="/screenshots/gameplay.gif" width="320" height="240" />

Walter's been cursed, but can he be cured?
Guide him through two frayed realities by warping through any obstacle before you. PyWeek April 2018 entry by Oscar Lin and Anas Elmi. Thank you PyWeek for organizing this event. The theme was two worlds.

## Requirements:
```
Python 3.6
Pygame 1.9.3
```
## Build
```
$ python3.6 ./main.py
```
# Controls

* WASD or arrow keys to move and jump
* Space to warp
* R to restart
* Escape to pause

# Assets used:
* player gfx https://jesse-m.itch.io/jungle-pack
* error sfx https://opengameart.org/content/interface-beeps
* teleport sfx https://opengameart.org/content/teleport
* warp charge https://kronbits.itch.io/matriax-free-assets
* collect warp charge jingle https://opengameart.org/content/4-sci-fi-menu-sounds (http://www.archive.org/details/TimMortimer)
* environment gfx https://opengameart.org/content/sci-fi-platform-tiles
* enemy gfx https://rvros.itch.io/pixel-art-animated-slime
* bgm https://opengameart.org/content/portal
* font https://fontlibrary.org/en


# Progression
## Day 1-3
![](/screenshots/day3-1.png)
![](/screenshots/day3-2.png)

Completed:
* player movement
* gravity
* camera system

Initially we were going to code a basic playable level as well but collision logic took longer than expected. TODO tomorrow

## Day 4
![](/screenshots/day4-1.png)
![](/screenshots/day4-2.png)
![](/screenshots/day4-3.png)
![](/screenshots/day4-4.png)

Completed:
* test level
* warping
* goal

## Day 5
* <img src="/screenshots/day5-dumb.gif" width="320" height="240" />

  Simple enemy akin to Goombas from Mario that change direction on contact with wall
  

* <img src="/screenshots/day5-follower.gif" width="320" height="240" />

  Follower that chases when player gets too close. Also demostrates freezing of enemies when traveling to an alternate world
  

Plant on lock down on mechanics tomorrow or the day after in order to start making progress on graphics and level design
