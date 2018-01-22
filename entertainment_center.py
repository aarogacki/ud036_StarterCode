import media
import fresh_tomatoes

# Creating movie objects with my fave movies

the_force_awakens = media.Movie("The Force Awakens",
                                "The darkside is messing everything up again",
                                "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",  # noqa
                                "https://www.youtube.com/watch?v=sGbxmsDFVnE")


big_hero_6 = media.Movie("Big Hero 6",
                         "Kid saves the world with giant marshmellow robot",
                         "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",  # noqa
                         "https://www.youtube.com/watch?v=z3biFxZIJOQ")

the_last_jedi = media.Movie("The Last Jedi",
                            "Rey is probably the last Jedi",
                            "https://upload.wikimedia.org/wikipedia/en/7/7f/Star_Wars_The_Last_Jedi.jpg",  # noqa
                            "https://www.youtube.com/watch?v=Q0CbN8sfihY")

moana = media.Movie("Moana",
                    "Girl saves village with Dwayne Johnson",
                    "https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg",  # noqa
                    "https://www.youtube.com/watch?v=LKFuXETZUsI")

monsters_inc = media.Movie("Monsters, Inc.",
                           "Monsters scare kids for electricity",
                           "https://upload.wikimedia.org/wikipedia/en/6/63/Monsters_Inc.JPG",  # noqa
                           "https://www.youtube.com/watch?v=8IBNZ6O2kMk")

mulan = media.Movie("Mulan",
                    "Woman impersonates a man and saves China",
                    "https://upload.wikimedia.org/wikipedia/en/a/a3/Movie_poster_mulan.JPG",  # noqa
                    "https://www.youtube.com/watch?v=MsAniqGowKE")

the_lion_king = media.Movie("The Lion King",
                            "A little lion cub grows up to be king",
                            "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",  # noqa
                            "https://www.youtube.com/watch?v=V6jOvVf05aQ")

the_phantom_menace = media.Movie("The Phantom Menace",
                                 "A boy decides to leave home to be a Jedi",
                                 "https://upload.wikimedia.org/wikipedia/en/4/40/Star_Wars_Phantom_Menace_poster.jpg",  # noqa
                                 "https://www.youtube.com/watch?v=bD7bpG-zDJQ")

rogue_one = media.Movie("Rogue One",
                        "A plot hole is filled",
                        "https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png",  # noqa
                        "https://www.youtube.com/watch?v=frdj1zb9sMY")

# Creating an array of my fave movies
movies = [the_phantom_menace, rogue_one, the_force_awakens, the_last_jedi,
          moana, big_hero_6, monsters_inc, mulan, the_lion_king]

# Calling the function to open up the webpage
fresh_tomatoes.open_movies_page(movies)
