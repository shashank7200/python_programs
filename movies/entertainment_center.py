import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=JcpWXaA2qeg")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien Planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)

#avatar.show_trailer()

gotg2= media.Movie("Guardians of the Galaxy Vol.2",
                   "A sequel to the Guardians of the Galaxy",
                   "https://upload.wikimedia.org/wikipedia/en/9/95/GotG_Vol2_poster.jpg",
                   "https://www.youtube.com/watch?v=pr7tDrwQ3t8")

gotg2.show_trailer()

ratatouille=media.Movie("Ratatouille","Storyline",
                        "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                        "https://www.youtube.com/watch?v=niD-jahFURU")


midnight_in_paris = media.Movie("Midnight in Paris", "Storyline",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY" )


hunger_games = media.Movie("Hunger Games", "Storyline",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

movies=[toy_story,avatar,gotg2,ratatouille,midnight_in_paris,hunger_games]

fresh_tomatoes.open_movies_page(movies)

