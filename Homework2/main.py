#Functions
def title():
    title = 'Hello'
    return title
    # print(title)


def artist():
    artist = 'Lionel Richie'
    return artist


def year():
    year = 1992
    return year


def genre():
    genre = 'Pop'
    if genre == 'Pop':
        return bool(genre)
    else:
        return genre

# Call Functions
title = title()
artist = artist()
year = year()
genre = genre()

#Print Values
print(title)
print(artist)
print(year)
print(genre)
