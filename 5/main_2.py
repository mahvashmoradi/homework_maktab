def get_data(_str):
    if _str == 'Book':
        title = input('enter title: ')
        author = input('enter author: ')
        publish_year = input('enter publish_year: ')
        pages = int(input('enter pages: '))
        language = input('enter Language: ')
        price = input('enter price: ')
        book = Book(title, author, publish_year, pages, language, price)
        return book
    elif _str == 'Magazine':
        title = input('enter title: ')
        author = input('enter author: ')
        publish_year = input('enter publish_year: ')
        pages = int(input('enter pages: '))
        language = input('enter Language: ')
        price = input('enter price: ')
        issue = input('enter issue: ')
        Mazine = Magazine(title, author, publish_year, pages, language, price, issue)
        return Mazine

    elif _str == 'Podcast':
        title = input('enter title: ')
        speaker = input('enter speaker: ')
        publish_year = input('enter publish_year: ')
        time = int(input('enter time: '))
        language = input('enter Language: ')
        price = input('enter price: ')
        pdepisode = PodcastEpisode(title, speaker, publish_year, time, language, price)
        return pdepisode
    elif _str == 'AudioBook':
        title = input('enter title: ')
        speaker = input('enter speaker: ')
        author = input('enter author: ')

        publish_year = input('enter publish_year: ')
        pages = int(input('enter pages: '))
        time = int(input('enter time: '))
        booklanguage = input('enter book_Language: ')
        audiolanguage = input('enter audio_Language: ')
        price = input('enter price: ')
        aubook = AudioBook(title, speaker, author, publish_year, pages, booklanguage, audiolanguage, time, price)
        return aubook
    else:
        print('Undefined input')


class Book:
    def __init__(self, title, author, publish_year, pages, language, price):
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.pages = pages
        self.language = language
        self.price = price
        self.read_tot = 0

    def read(self, read_x):
        self.read_tot += read_x
        cal_page = self.pages - self.read_tot
        if cal_page < 0:
            print("You are completing the book")
        elif cal_page > 0:
            print(f"you have read {read_x} more pages from {self.title}. There are {cal_page} pages left")

    def get_status(self):
        cal_status = lambda x: 'unread' if (x == 0) else 'reading' if (x < self.pages) else 'finished'
        print(cal_status(self.read_tot))

    def __str__(self):
        return f"{self.title, self.author, self.publish_year, self.pages, self.language, self.price}"


class Magazine(Book):

    def __init__(self, title, author, publish_year, pages, language, price, issue):
        Book.__init__(self, title, author, publish_year, pages, language, price)
        self.issue = issue


class PodcastEpisode(Book):

    def __init__(self, title, speaker, publish_year, time, language, price):
        Book.__init__(self, title=title, publish_year=publish_year, language=language, price=price, author=None,
                      pages=None)
        self.speaker = speaker
        self.time = time


class AudioBook(Book):
    def __init__(self, title, speaker, author, publish_year, pages, booklanguage, audiolanguage, time, price):
        Book.__init__(self, title, author, publish_year, pages, price=price, language=None)
        '''PodcastEpisode.__init__(self, title=title, speaker=speaker, time=time, language=None, publish_year=None,
                                price=None)'''
        self.speaker = speaker
        self.time = time
        self.booklanguage = booklanguage
        self.audiolanguage = audiolanguage


list_book = []
while (True):
    _str = input(
        "please enter the type of your media\n 'Book', 'Magazine', 'Podcast', 'AudioBook'.\n Type Quit when your media finish:  ")
    if _str == 'Quit':
        break
    else:
        list_book.append(get_data(_str))
# list_book = [Book('No Friend But the Mountains', 'Behrouz Boochani', '2018', 374, 'English', '10'),
#             Book('The Black Swan', 'Abbas Maroufi', '2007', 280, 'Percian', '20'),
#             Book('Symphony of the Dead', 'Behrouz Boochani', '2018', 374, 'English', '126')]
print('---------------------List of books--------------------')
[print(i) for i in list_book]

'''list_book[0].read(20)
list_book[2].read(200)
list_book[2].read(200)
list_book[0].get_status()
list_book[1].get_status()
list_book[2].get_status()'''
