# Goal #1: Create a program that will print out a list of movie titles and a set of ratings defined below into a particular format.
# Once all of your information is stored in lists, loop through those lists to print out information with each part separated by a comma, like this:

# Example:
# Jurassic Park, PG-13, 3, 8.0, Adventure / Sci-Fi
# Back to the Future, PG, 1, 8.5, Adventure / Comedy / Sci-Fi


movies = ['Skyfall', 'Argo', 'Lincoln', 'Brave', 'Arbitrage']

pg_rating = ['PG-13','R', 'PG-13','PG', 'R']
bechdel_test= ['3', '3', '3', '3', '2']
imdb_rating=['7.8','7.8', '7.5', '7.2', '6.7']
genre=['Action', 'Drama', 'Drama', 'Animation', 'Thriller']


list = [movies, pg_rating, bechdel_test, imdb_rating,genre]
no=0
for each in list:
	print movies[no],",", pg_rating[no], ",",bechdel_test[no],",", imdb_rating[no],",",genre[no]
	no=no+1
