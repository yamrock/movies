import webbrowser

class Movie():
    '''
    Defines the class attributes for the instances. Requires the following:
    1. Movie Name
    2. Short description
    3. Link to an image
    4. Link to youtube trailer
    '''
    def __init__(self, movie_title, movie_storyline, poster_image, trailier_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailier_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
