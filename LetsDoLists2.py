import time

favorite_artists = ['cuco', 'nofx', 'slayer', 'type-o-negative', '2pac', 'nina simone', 'anal cunt']
print('\nHere are some of my favorite artists')
for item in favorite_artists:
    print(item.title())
time.sleep(2)

favorite_artists[2] = 'prince'
favorite_artists[3] = 'megadeth'
time.sleep(2)

print("\nNevermind, this is them")
for item in favorite_artists:
    print(item.title())

favorite_artists.append('smashing pumpkins')
favorite_artists.append('pink floyd')
favorite_artists.append('less than jake')

time.sleep(2)

print("\nOk, I added a few more to my list:")

for item in favorite_artists:
    print(item.title())
    
del favorite_artists[3]
del favorite_artists[5]

print("\nOk, I took some off the list.")

for item in favorite_artists:
    print(item.title())
    
removed_artists = favorite_artists.pop()
print(f"\nI'm taking this one off of my list:\n{removed_artists.title()}")


