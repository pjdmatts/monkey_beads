import media
import fresh_tomatoes

#generate instances of the class Movie to store title, storyline, poster art
#and Youtube video

toy_story = media.Movie("Toy Story", "The Toys Are Alive?!",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A Marine Goes Camping With Some Tall Blue People",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

north_by_northwest = media.Movie("North By Northwest",
                                 "Running Away From Planes While Keeping Hair Nice",
                                 "https://upload.wikimedia.org/wikipedia/commons/8/83/Northbynorthwest1.jpg",
                                 "https://www.youtube.com/watch?v=VZmbbx2p4yI")

big_lebowski = media.Movie("The Big Lebowski",
                           "Bowling, Cardigans and Beards",
                           "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
                           "https://www.youtube.com/watch?v=VgSqm8-wXWA")

the_martian = media.Movie("The Martian",
                          "Potatoes, Anyone?",
                          "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                          "https://www.youtube.com/watch?v=XQnYm5MG1x0")

harry = media.Movie("The Trouble With Harry",
                    "How To Dispose Of A Corpse In Beautiful Vermont",
                    "https://upload.wikimedia.org/wikipedia/commons/c/c2/The_Trouble_with_Harry.jpg",
                    "https://www.youtube.com/watch?v=U0w_1cHIc-0")

#store the movie objects in a list and pass to the method within fresh_tomatoes
#that will generate the web page.

movies = [toy_story, avatar, north_by_northwest,
          big_lebowski, the_martian, harry]

fresh_tomatoes.open_movies_page(movies)
