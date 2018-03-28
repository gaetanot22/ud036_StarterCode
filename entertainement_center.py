import media
import fresh_tomatoes

# Create all the movies information
# Creates instance StarWarsXXX of Movie class by calling class constructor
StarWarsI = media.Movie("Star Wars Episode I - The Phantom menace",
                        "https://upload.wikimedia.org/wikipedia/en/4/40/Star_Wars_Phantom_Menace_poster.jpg",
                        "https://www.youtube.com/watch?v=bD7bpG-zDJQ")

StarWarsII = media.Movie("Star Wars Episode II - Attack of the Clones",
                         "https://upload.wikimedia.org/wikipedia/en/3/32/Star_Wars_-_Episode_II_Attack_of_the_Clones_%28movie_poster%29.jpg",
                         "https://www.youtube.com/watch?v=gYbW1F_c9eM")

StarWarsIII = media.Movie("Star Wars Episode III - Revenge of the Sith",
                          "https://upload.wikimedia.org/wikipedia/en/9/93/Star_Wars_Episode_III_Revenge_of_the_Sith_poster.jpg",
                          "https://www.youtube.com/watch?v=5UnjrG_N8hU")

StarWarsIV = media.Movie("Star Wars Episode IV - A new hope",
                         "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                         "https://www.youtube.com/watch?v=367FSjWvNB4")

StarWarsV = media.Movie("Star Wars Episode V - The empire strikes back",
                        "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                        "https://www.youtube.com/watch?v=JNwNXF9Y6kY")

StarWarsVI = media.Movie("Star Wars Episode VI - Return of the Jedi",
                         "https://upload.wikimedia.org/wikipedia/en/b/b2/ReturnOfTheJediPoster1983.jpg",
                         "https://www.youtube.com/watch?v=5UfA_aKBGMc")

StarWarsVII = media.Movie("Star Wars Episode VII - The force awakens",
                          "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
                          "https://www.youtube.com/watch?v=sGbxmsDFVnE")

StarWarsVIII = media.Movie("Star Wars Episode VIII - The last Jedi",
                           "https://upload.wikimedia.org/wikipedia/en/7/7f/Star_Wars_The_Last_Jedi.jpg",
                           "https://www.youtube.com/watch?v=HqVSuqJrU1I")

StarWarsStoryI = media.Movie("Rogue one - a Star Wars Story",
                             "https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png",
                             "https://www.youtube.com/watch?v=frdj1zb9sMY")

# Collect all movie in a list in order to pass to the open_movies_pages function
movies = [StarWarsI, StarWarsII, StarWarsIII, StarWarsIV, StarWarsV, StarWarsVI, StarWarsVII, StarWarsVIII, StarWarsStoryI]

# Generates HTML page with all the movies
fresh_tomatoes.open_movies_page(movies)
