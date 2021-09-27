# https://www.interviewcake.com/question/python3/inflight-entertainment?course=fc1&section=hashing-and-hash-tables
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 


def calculate_movie_pairs(flight, movies):

    movies_list = movies

    for movie in movies_list:
        print(movie)
        movies_list.pop(movies_list.index(movie))

        # this has a n^2 runtime, so other better options are: 
        # sort the list then index pairs from each sorted end, i.e. i ++ and -1 -1
        for pair in movies_list:
            if movie + pair < flight:
                print(True)
                return True
            else:
                pass


flight_length = 240
movie_lengths = [10, 120, 119, 150, 100, 199]

calculate_movie_pairs(flight_length, movie_lengths)











# # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# You've built an inflight entertainment system with on-demand movie streaming.

# Users on longer flights like to start a second movie right when their first one ends, but they complain that the plane usually lands before they can see the ending. So you're building a feature for choosing two movies whose total runtimes will equal the exact flight length.

# Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes) and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.

# When building your function:

#     Assume your users will watch exactly two movies
#     Don't make your users watch the same movie twice
#     Optimize for runtime over memory


