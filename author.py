# Part 1 & 2: Author Class with No Duplicate Books and Formatted Output

class Author:
    def __init__(self, name: str):
        # Initialize the author's name and empty list of books
        self.name = name
        self.books = []

    def publish(self, title: str):
        # Only add book if it's not already published
        if title in self.books:
            print(f"Error: '{title}' is already published by {self.name}.")
        else:
            self.books.append(title)

    def __str__(self):
        # Format books with quotes and commas, display author name above
        books_formatted = [f'"{book}"' for book in self.books]
        return f"{self.name}\n{books_formatted}"


def main():
    # Create some authors
    author1 = Author("Maya Angelou")
    author2 = Author("J.K. Rowling")

    # Publish books
    author1.publish("I Know Why the Caged Bird Sings")
    author1.publish("Phenomenal Woman")
    author1.publish("I Know Why the Caged Bird Sings")  # Duplicate test

    author2.publish("Harry Potter and the Sorcerer's Stone")
    author2.publish("Harry Potter and the Chamber of Secrets")

    # Print authors and their books
    print(author1)
    print()
    print(author2)


# Run the main function
if __name__ == "__main__":
    main()
