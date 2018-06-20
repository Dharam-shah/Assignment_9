class Movie:

    def __init__(self,M_name,art_name,rel_year,rating):
        self.M_name = M_name
        self.art_name = art_name
        self.rel_year = rel_year
        self.rating = rating

    def display(self):
        print('M_name: {}, art_name: {}, rel_year: {}, rating: {},'. \
              format(self.M_name, self.art_name, self.rel_year, self.rating))

m1 = Movie('Race-3', 'salman khan', 2018, 4)
m1.display()

m2 = Movie('veer_zara', 'sharukh_khan', 2004, 5)

m2.display()