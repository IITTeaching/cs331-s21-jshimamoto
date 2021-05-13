import urllib
import urllib.request

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    lst = book_to_words()
    longest = len(max(lst,key = len)) - 2
    sorted = countSort(lst, longest + 1)
    for i in range(longest, -1, -1):
        sorted = countSort(sorted, i)
    return sorted

def countSort(lst, num):
    counter = [0] * 128
    shi = [None] * len(lst)
    for i in lst:
        if len(i) - 1 < num:
            k = 0
        else:
            k = ord(i.decode('ascii')[num])
        counter[k] += 1
    for i in range(1, len(counter)):
        counter[i] += counter[i - 1]
    for i in range(len(lst) - 1, -1, -1):
        if len(lst[i]) - 1 < num:
            k = 0
        else:
            k = ord(lst[i].decode('ascii')[num])
        shi[counter[k] - 1] = lst[i]
        counter[k] += -1
    return shi
print(radix_a_book())