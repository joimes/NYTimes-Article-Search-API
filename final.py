# Your code must

# Use the New York Times API to retrieve data.
# Select and/or transform the retrieved data.
# Write data to a file.
import requests
from textblob import TextBlob
def articleSearch():
    '''Main function that searches for an article, based on keyword(s)'''
    key = 'NYTimes_Article_Search_key'
    numberError = True
    menuRepeat = True
    while(menuRepeat == True):
        query = input("What game would you like to search?\n")
        queryblob = TextBlob(query)

        if(queryblob != queryblob.correct()):
            while(numberError == True):
                answer = input("Did you mean " + '"' + str(queryblob.correct()) + '"' + "? (1 for yes, 2 for no)\n")
                if(answer == '1'):
                    query = queryblob.correct()
                    numberError = False
                elif(answer == '2'):
                    query = queryblob
                    numberError = False
                else:
                    print("\nTry again. (1 for yes, 2 for no)")
                    numberError = True

        print(query)



# URL for the technology page w/ API key
        url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?q={query}&api-key={key}'
# Get the data
        data = requests.get(url)

# Turn data into JSON
        import json
        data = data.json()

#print(data['response']['docs'][1]['headline']['main'])
# Write
        try:
            myfile = open('gamingnews.txt', 'w')
            i = 1
            for article in data['response']['docs']:
                test = TextBlob(article['headline']['main'])
                count = test.noun_phrases.count(query)
                myfile.write(str(i) + ': ' + article['headline']['main'] + " n = " + str(count) + '\n')
                i+=1
            myfile.close()
# Read
            myfile = open('gamingnews.txt', 'r')
            for file in myfile:
                print(file)

            myfile.close()
        except:
            print("\nNo news found on this game. Sorry. :'[\n")
    # Ask the user if they want to do another search
        menuError = True
        while(menuError == True):
            menuAnswer = input("Would you like to search again? (1 for yes, 2 for no)\n")
            if (menuAnswer == '1'):
                menuRepeat = True
                menuError = False
            elif(menuAnswer == '2'):
                print("\nThanks for using my Video Game Search API. Goodbye!\n")
                menuRepeat = False
                menuError = False
            else:
                print("\nTry again. (1 for yes, 2 for no)")
                menuError = True

# Main
articleSearch()
