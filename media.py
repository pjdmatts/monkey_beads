import webbrowser

class Movie:
    """
	This class provides a way to store movie related information
	Usage:
		This class is used to create instance of the class Movie, passing in
		the required variables.
		example:
		toy_story = media.Movie("Toy Story", "The Toys Are Alive?!",
			                    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
			                    "https://www.youtube.com/watch?v=vwyZH85NQC4")
	Instance Variables:
		movie_title, the title of the movie
		movie_storlyine, a short one sentence overview of the movie
		poster_image, a url for an example of the movies poster art
		trailer_youtube, a url for a trailer on youtube
	"""
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
