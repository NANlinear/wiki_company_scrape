import wikipedia
import requests
import wptools

# Python Wikipedia library
search = wikipedia.WikipediaPage("Jaguar Cars")
# print(search.html())

search = "Jaguar_Cars"

page = wptools.page(search)
d = page.get_parse()
print(d.data['infobox'])

# NOTES: okay this library allows us to extract infobox data pretty easily 
# https://github.com/siznax/wptools 

