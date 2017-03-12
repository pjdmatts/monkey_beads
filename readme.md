**Entertainment Center**

***What is this code for?***

`entertainment_center.py` is a script that allows you to store information
about your favorite movies (using a class set up in `media.py`) and have the
`fresh_tomatoes.py` module build a web page that showcases the movies
and allows the use to view the movies trailers.

***Where to get the files***

Download the necessary files from [this Github repository](https://github.com/pjdmatts/monkey_beads)

***Files Included***

- `fresh_tomatoes.py` a script to generate a web page that shows the movies
and their trailers.

- `main.css` custom css that overrides some of the Bootstrap defaults

- `entertainment_center.py` a script to store information about the movies

- `media.py` a class that provides a way to store movie related information

***Requirements***

This code was written with Python 2.7.13.

***How to use this application***

Navigate to the root of the application and in a terminal type:
```
python entertainment_center.py

```
A browser window (or new tab if you already have a browser open) will open
with a web-page that shows the movies contained in `entertainment_center.py`
Hovering over a poster will show a short description of the film.
Clicking on a poster will play that movies trailer.

***ToDo***

- Modify the Bootstrap Navbar. Hoping that the next step of the course will
cover this.

- Add an Admin Interface to allow updates to the movies from the browser.

- Add access to [IMBD database](http://www.imdb.com/)
