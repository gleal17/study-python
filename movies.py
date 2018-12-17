import media
import webmovie
toy_story = media.Movie("ToyStory",
                        "Toy story...\n",
                        "https://imgc.allpostersimages.com/img/print/posters/toy-story-woody-buzz_a-G-13390941-0.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

# print(toy_story.storyline)

inception = media.Movie ("Inception",
            "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
            "https://images-na.ssl-images-amazon.com/images/I/61Ug%2BK8o5FL.jpg",
            "https://www.youtube.com/watch?v=d3A3-zSOBT4")

#print(inception.storyline)
movies =[toy_story, inception]

webmovie.open_movies_page(movies)


