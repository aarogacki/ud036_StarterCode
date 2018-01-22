import webbrowser


class Movie():

	"""Class blueprinting future movie objects
    movie_title: title of movie
    movie_storyline: One sentence description
    poster_image: Movie poster jpg
    trailer_youtube: Url from youtube
    Methods:
    show_trailer: opens up the youtube_url in your browser
    """
    # Init - will initialize the object using the given args
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Method using the imported webbrowser

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
