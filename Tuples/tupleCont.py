# tuples can contain elements that are themselves tuples

# example 1
imelda = "More Mayhem", "Emilda May", 2011, (
    (1, "Pulling the Rug"),
    (2, "Psycho"),
    (3, "Mayhem"),
    (4, "Kentish Town Waltz")
)
print(imelda)

# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)
# print(tracks)


# extrtacting each individual tuple
title, artist, year, track1, track2, track3, track4 = imelda
print(title)
print(artist)
print(year)
print(track1)
print(track2)
print(track3)
print(track4)

# tuple with lists
imelda_with_lists = "More Mayhem", "Emilda May", 2011, (
    [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])

imelda_with_lists[3].append((5, "All for you"))
title, artist, year, tracks = imelda_with_lists
tracks.append((6,"Eternity"))

for song in tracks:
    track, title = song
    print("\t Track number {}, Title: {}".format(track,title))