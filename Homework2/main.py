
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


title = title()
artist = artist()
year = year()
genre = genre()

print(title)
print(artist)
print(year)
print(genre)
