"""
They have delivered you a string that contains a list of poems, titled highlighted_poems, they want to highlight on the site, but they need your help to parse the string into something that can display the name, title, and publication date of the highlighted poems on the site.

"""
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print("\tList of informations :\n")
highlighted_poems_list = highlighted_poems.split(',')
highlighted_poems_stripped=[]
highlighted_poems_details = []

#
titles= []
poets = []
dates = []

for index_0 in highlighted_poems_list:
  index_striped = index_0.strip()
  highlighted_poems_stripped.append(index_striped)
for index_1 in highlighted_poems_stripped :
  index_splited = index_1.split(':')
  highlighted_poems_details.append(index_splited)
for index_3 in highlighted_poems_details :
    titles.append(index_3[0])
    poets.append(index_3[1])
    dates.append(index_3[2])
#
for i in range(len(titles)):
    print("The poem {TITLE} was published by {POET} in {DATE}.".format(
        TITLE=titles[i],POET=poets[i],DATE=dates[i]
    ))

     
    