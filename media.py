class Movie():
    """class to create a movie-trailer website"""
    def __init__(self, movie_title, movie_storyline,
                 movie_poster_url, movie_youtube_url):
        """Current instance of class Movie"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_url
        self.trailer_youtube_url = movie_youtube_url
