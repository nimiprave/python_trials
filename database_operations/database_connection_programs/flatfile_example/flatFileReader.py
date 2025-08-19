# Example of reading the flat file.
import csv


def reading_the_csv():
    with open("author_book_publisher.csv", ) as csv:
        records = csv.readlines()
        for line in records:
            print(line)


if __name__ == "__main__":
    reading_the_csv()
