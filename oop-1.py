# Add methods to the class to give it the ability to:
#   - Go directly to a specific page number
#   - Bookmark a specific page number, i.e. not just the current page
#   - Automatically go back to the start of the book (i.e. page 1) when the user turns the final page


class Book:

    # Sets the attributes for a Class Object
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.current_page = 1
        self.bookmark = 1
        self.bookmark_add = 1

    def bookmark_current_page(self):
        self.bookmark = self.current_page
    
    def bookmark_add_page(self, page):
        self.bookmark_add = page

    def move_to_page(self, page):
        self.current_page = page

    def turn_page(self, forward):
        if forward:
            self.current_page += 1
            if self.current_page <= self.num_pages:
                pass
            else:
                self.current_page = 1
        else:
            self.current_page -= 1

    def __len__(self):
        return self.num_pages

    # Overrides default print for the Class Object
    def __str__(self): 
        return f"Title: {self.title}, Author: {self.author}"

google_book = Book("How Google Works", "Google Founders", 200)
print(google_book)
print(google_book.current_page)
google_book.move_to_page(199)
print(google_book.current_page)
google_book.turn_page(True)
print(google_book.current_page)
google_book.turn_page(True)
print(google_book.current_page)
print(f"Bookmark: {google_book.bookmark_add}")
google_book.bookmark_add_page(155)
print(google_book.bookmark_add)