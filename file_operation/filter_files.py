lyrics = '''Well, my friends, the time has come
To raise the roof and have some fun
Throw away the work to be done
Let the music play on (play on, play on, play on...) Everybody sing, everybody dance
Lose yourself in wild romance
We're going to Party, Karamu, Fiesta, forever Come on and sing along!
All night long (all night), All night (all night) All night long (all night), All night (all night) All night long (all night), All night (all night) All night long! (all night), Ooh, yeah (all night)
People dancing all in the street
See the rhythm all in their feet
Life is good, wild and sweet
Let the music play on...(Play on, play on, play on...) Feel it in your heart and feel it in your soul
Let the music take control
We're going to Party, We're going to Party,
with open("song.txt", file.write(lyrics)
Liming, Fiesta, forever Come on and sing along Liming, Fiesta, forever Come on and sing my song!'''

with open("song.txt", "w+") as file:
  file.write(lyrics)

def word_search(filename, word): 
  with open(filename, "r+") as file:
    for line in file: 
      if word in line:
        print(line)

word_search("song.txt", "sing")
