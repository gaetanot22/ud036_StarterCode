import webbrowser

class Movie():
    """ Movie class used to store movie related information.

    Attributes:
    movie_title: Movie Title
    poster_image: Poster image link
    trailer_youtube: Trailer youtube link
    """

    # class constructor
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # method used to display movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
