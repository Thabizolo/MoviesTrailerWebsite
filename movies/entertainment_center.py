import fresh_tomatoes
import media

""" In this file I create multiple instances of the"""
""" Movie Class to represent my favorite movies"""

toy_story = media.Movie("Toy Story",
                        "A boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/" +
                        "Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=JcpWXaA2qeg")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar" +
                     "-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

lord_of_the_rings = media.Movie("Lord Of the Rings",
                                "A ring that causes trouble with hobits",
                                "https://upload.wikimedia.org/wikipedia/en" +
                                "/9/9d/The_Lord_of_the_Rings_" +
                                "The_Fellowship_of_the_Ring_" +
                                "%282001%29_theatrical_poster.jpg",
                                "https://www.youtube.com/watch?v=r5X-hFf6Bwo")

scarface = media.Movie("Scarface",
                       "A story about a colombian who makes" +
                       "it big time in USA",
                       "https://upload.wikimedia.org/wikipedia/en" +
                       "/7/71/Scarface_-_1983_film.jpg",
                       "https://www.youtube.com/watch?v=7pQQHnqBa2E")

the_lion_king = media.Movie("The Lion King",
                            "A rivetting story about a young lion" +
                            "who becomes a king",
                            "https://vignette.wikia.nocookie.net/" +
                            "disney/images" +
                            "/c/cb/The_Lion_King_Textless_poster_1.jpg" +
                            "/revision/" +
                            "latest?cb=20140810104158",
                            "https://www.youtube.com/watch?v=4sj1MT05lAA")

kung_fu_panda = media.Movie("Kung Fu Panda",
                            "A story about a panda who becomes" +
                            "the dragon worrier",
                            "https://upload.wikimedia.org/wikipedia/en/7/76/" +
                            "Kungfupanda.jpg",
                            "https://www.youtube.com/watch?v=PXi3Mv6KMzY")

"""group all the instances together in a list."""
movies = [toy_story, avatar,
          lord_of_the_rings,
          scarface, the_lion_king,
          kung_fu_panda]

"""Using the fresh_tomatoes starter code to call method open_movies_page
that takes in one argument, which is a list of movies, and creates an HTML
file which will display all of your favorite movies."""
fresh_tomatoes.open_movies_page(movies)
