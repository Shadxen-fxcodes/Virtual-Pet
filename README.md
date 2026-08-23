# Pet Racer 🏎️

This is a small project that I made to start of StarDance. I got awfully busy so had to postpone the designing and everything. To begin with, this is heavily inspired by Tamagotchi children mini pet toy and the Disney Pixar Cars character, #95 Lightning McQueen. Initially, I tried to do this using Python as the elected programming language, but if you take a quick look at my first few dev logs, it was frankly a bit mid, so I switched to JavaScript. I hope you, as the consumer have a little bit of fun trying out this little project that I made. It's meant to be a bit of a time-pass kind of game, not your average AAA game unfortunately :(, but here we are! Happy Gaming!!

![Virtual Pet Banner](./img/Mainmenu.png)

---

### Notes for Stardance Reviewers

#### Originality
* Wanted to make a dynamic racer with an Tamagotchi style game instead of a standard text or puzzle game.
* Built a real-time pit management mechanic so you actually have to balance your speed against car wear and tear.
* Created custom touch controls so it works cleanly on mobile devices without needing a keyboard.
* Composed the main menu soundtrack myself.

![Gameplay Preview](./img/garage.png)

#### Technical Details
* **Vanilla Stack:** Built entirely with plain HTML, CSS, and pure JavaScript inside `pet_racer.html` without heavy third-party libraries.
* **Vehicle State Loop:** Tracks speed, tire wear, and engine heat dynamically. Overusing nitro or taking sharp turns degrades your vehicle stats.
* **Dual Input System:** Listens for active input type and seamlessly toggles between keyboard bindings and on-screen touch thumb pads.
* **Mid-Race Pit Actions:** Mapped keys `1` through `6` to repair specific components on the fly without pausing the canvas loop.
* **Local Storage:** Saves garage unlocks and high scores directly to the browser.

![Gameplay Preview](./img/mods.png)

#### Usability & Polish
* This game should play instantly in Chrome, Safari, Edge, or Firefox with no apparent problem.
* Mobile UI uses a simple thumb pad placement so your hands don't cover the main track view (it isn't fully tested, but as far as I know it should work OK).
* Cleaned up the CSS layout to keep the frame rate steady on lower-end hardware.

#### Storytelling & Devlogs
* Documented the build process on Stardance itself, covering bug fixes and feature iteration. Check out the dev logs to see how the project came together.

![Gameplay Preview](./img/logbook.png)

---

### Controls

#### 💻 Desktop
* **Steer:** `A` / `D` or `←` `→`
* **Throttle:** `W` or `↑`
* **Brake / Reverse:** `S` or `↓`
* **Nitro:** `SPACE`
* **Pit Actions:** `1` – `6`
* **Pause:** `P` or `ESC`

#### 📱 Mobile
* **Steering:** Left on-screen thumb pad
* **Throttle / Brake:** Right on-screen thumb pad
* **Nitro & Pit Actions:** On-screen buttons

---

### Recent Updates
* **CSS Refactor:** Updated menu layouts and improved overall UI responsiveness on mobile screens.
* **Code Polish:** Cleaned up the main game loop and rewrote initial draft code to ensure the entire script is hand-crafted and lightweight.

---

### Known Issues
* The mobile edition isn't fully tested as of yet as it does take some time to fully wring out the game mechanics.
* Please do note this game is made entirely on my computer so obviously it will be a more PC focused design language and UI that may not be fully suited to all mobile devices.
* It is my exam season so I wasn't able to put 100% effort into this but please do try it out.

---

### About
A browser-based pet racing game built with HTML, CSS, and Vanilla JavaScript.
