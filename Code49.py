class Book:
    def __init__(self,title="",author="",publisher="",price=0,copies=0,author_royality=0):
        self._title=title
        self._author=author
        self._publisher=publisher
        self._price=price
        self._copies=copies
        self._authors_royalty=author_royality

    def get_title(self):
        return self._title

    def set_title(self,x):
        self._title=x

    title=property(get_title,set_title)

    def get_author(self):
        return self._author

    def set_author(self,y):
        self._author=y

    author=property(get_author,set_author)

    def get_publisher(self):
        return self._publisher

    def set_publisher(self,y):
        self._publisher=y

    publisher=property(get_publisher,set_publisher)

    def get_price(self):
        return self._price

    def set_price(self,y):
        self._price=y

    price=property(get_price,set_price)

    def get_copies(self):
        return self._copies

    def set_copies(self,y):
        self._copies=y

    copies=property(get_copies,set_copies)

    def royalty(self):
        if self._copies>=500:
            self._authors_royality=10/100*self._price
        if self._copies>=1000:
            self._authors_royality=12.5/100*self._price+self._authors_royality
        else:
            self._authors_royality=15/100*self._price+self._authors_royality
        return self._authors_royality



class Ebook(Book):
    def __init__(self,format="",title="",author="",publisher="",price=0,copies=0,author_royality=0):
        Book.__init__(self,title,author,publisher,price,copies,author_royality)
        self._format=format

    def set_format(self,x):
        self._format=x

    def get_format(self):
        return self._format

    def royalty2(self):
        x=self.royalty()
        return x*88/100




little=Book()
little.set_title("Harry")
little.set_author("J.K.")
little.set_publisher("Wildcart")
little.set_price(900)
little.set_copies(10000)

print("************************************************************\n\n")
print(little.get_title())
print(little.get_author())
print(little.get_publisher())
print(little.get_price())
print(little.get_copies())
print(little.royalty(),"\n\n")

Little=Ebook()

print("*************************************************************")

Little.format="pdf"
Little.title="Secret of Nagas"
Little.author="Amish"
Little.publisher="Asde"
Little.price=900
Little.copies=50000

print("***********************************************************\n\n")
print(Little.format)
print(Little.title)
print(Little.author)
print(Little.publisher)
print(Little.price)
print(Little.copies)
print(Little.royalty2(),"\n\n")
print("************************************************************")
