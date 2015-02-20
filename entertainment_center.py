import media
import fresh_tomatoes

'''
This program creates instances of the class Movie, which requires the following attributes:
1. Movie Name
2. Short description
3. Link to an image
4. Link to youtube trailer

It then calls the redering function in fresh_tomatoes to build the html page to display the movies.
'''

toy_story = media.Movie("Toy Story", "A story about a boy and his toys",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar", "A marine in an alien world",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

TBL = media.Movie("TBL",
                  "I'm not Lebowski, I'm the Dude...",
                  "http://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
                  "https://www.youtube.com/watch?v=cd-go0oBF4Y")

manhattan = media.Movie("Manhattan", "A Neurotic in New York",
                        "http://upload.wikimedia.org/wikipedia/en/f/f3/Manhattan-poster01.jpg",
                        "https://www.youtube.com/watch?v=x7TuFo_Y0ys")

pulp_fiction = media.Movie("Pulp Fiction", "Gangsters everywhere",
                           "http://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

clockwork_orange = media.Movie("Clockwork Orange", "Psychotic conditioning/Re-hab",
                               "http://upload.wikimedia.org/wikipedia/en/4/48/Clockwork_orangeA.jpg",
                               "https://www.youtube.com/watch?v=G7fO3bzPeBQ")


movies = [toy_story, avatar, TBL, manhattan, pulp_fiction, clockwork_orange]

fresh_tomatoes.open_movies_page(movies)
                           

                        

