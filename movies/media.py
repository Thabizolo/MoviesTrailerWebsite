class Movie():
    """ this class creates a Data structure
        to store all favorite movies, including movie title,
        box art URL (or poster URL) and a YouTube link to the movie trailer."""

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
