import media
import fresh_tomatoes

# Information about Movie 1
wonder_woman = media.Movie("Wonder Woman",
                           "American superhero movie based on DC character",
                           "https://www.warnerbros.com/sites/default/files/styles/key_art_270x400/public/movies/media/browser/wonder_woman_whv_keyart.jpg?itok=cihiSYDU",  # NOQA
                           "https://www.youtube.com/watch?v=VSB4wGIdDwo")  # NOQA

# Information about Movie 2
the_jungle_book = media.Movie("The Jungle Book",
                              "Movie based on a book by Rudyard Kipling",
                              "http://t1.gstatic.com/images?q=tbn:ANd9GcQgNaB5wtt0G7_mTFVygkFtmjWut_Z0QSz2GzDsHeiZDHno4fjh",  # NOQA
                              "https://www.youtube.com/watch?v=C4qgAaxB_pc")  # NOQA

# Information about Movie 3
inside_out = media.Movie("Inside Out",
                         "American computer-animated psychological"
                         "comedy-drama film",
                         "http://t0.gstatic.com/images?q=tbn:ANd9GcTtZdvrahQxfjGkSBJCS-uiZKUfJNH4ddsqgCbV5oFkQiQ-tszE",  # NOQA
                         "https://www.youtube.com/watch?v=_MC3XuMvsDI")  # NOQA

# Information about Movie 4
spectre = media.Movie("Spectre",
                      "Spy film in James Bond film series",
                      "http://t3.gstatic.com/images?q=tbn:ANd9GcQcjheOnBb_WFU5yuYLnUYWjfr33KzdFx1PCNGVhgM4-89otmi9",  # NOQA
                      "https://www.youtube.com/watch?v=z4UDNzXD3qA")  # NOQA

# Information about Movie 5
doctor_strange = media.Movie("Doctor Strange",
                             "American superhero film based on the"
                             "Marvel Comics character",
                             "http://t3.gstatic.com/images?q=tbn:ANd9GcSmG4ms8wxdnuKOwetpc4qltTv7pHopDLRTi-t98dx-L-kt_b1t",  # NOQA
                             "https://www.youtube.com/watch?v=HSzx-zryEgM")  # NOQA

# Information about Movie 6
pretty_woman = media.Movie("Pretty Woman",
                           "A 1990 American romantic comedy film",
                           "http://t3.gstatic.com/images?q=tbn:ANd9GcSt9hkzW8Ubjyu-_4fdFK4XSI3BpZ02EPrz8Gxyfo64BiOqvRms",  # NOQA
                           "https://www.youtube.com/watch?v=Wzii8IuL8lk")  # NOQA

# List of movie objects
movies = [wonder_woman, the_jungle_book, inside_out, spectre,
          doctor_strange, pretty_woman]


fresh_tomatoes.open_movies_page(movies)
