import wikipedia as wk
import bottle
from bottle import route, run, template, request, get, post

HOST = "localhost"
PORT = "8080"

# Display Home Page - html page stored in template "home.tpl". Search criteria is input using an HTML form and passed to getSummary() function
@route('/')
def home():
    output = template("home.tpl")
    return output

# Display page containing summary of the Wikipedia page satisfying the search criteria input on the home page, after checking whether the page exist or whether
# the search criteria is too ambiguous to refer to a single page. The latter is done by getPage() function. 
@route('/summary', method="POST") 
def getSummary():
    keyword = request.forms["keyword"]
    length = request.forms["length"]
    lang = setLang(request.forms["lang"])
    page = getPage(keyword, length)
    try: 
        summary = wk.summary(keyword, sentences=length)
    except wk.DisambiguationError as e:
        return page
    except wk.exceptions.PageError:
        return "No page exists" + "<p><a href=\"\/" + HOST + ":" + PORT + "\">Back to home page</a>"
    else: 
        link = "<p><a href=\"" + page.url + "\">full Wikipedia article</a>" 
        backlink = "<p><a href=\"\/" + HOST + ":" + PORT + "\">Back to home page</a>"
        return "<h1>" + keyword + "</h1><p>" + summary + link + backlink 

@route('/summarydrop', method="POST")
def getSummaryDrop():
    keyword = request.forms.get('dropdown')
    length = request.forms["lengthPassed"]
    page = getPage(keyword, length)
    try:
        summary = wk.summary(keyword, sentences=length)
    except wk.DisambiguationError as e:
        backlink = "<p><a href=\"\/" + HOST + ":" + PORT + "\">Back to home page</a>"
        return page + backlink  
    except wk.exceptions.PageError:
        return "No page exists" + "<p><a href=\"\/" + HOST + ":" + PORT + "\">Back to home page</a>"
    else: 
        link = "<p><a href=\"" + page.url + "\">full Wikipedia article</a>"
        backlink = "<p><a href=\"\/" + HOST + ":" + PORT + "\">Back to home page</a>"
        return "<h1>" + keyword + "</h1><p>" + summary + link + backlink 

@route('/suggest', method="POST")
def getPage(keyword, length):
    try:
        page = wk.page(keyword)
    except wk.DisambiguationError as e:
        title = "<h1>Suggestions for " + '\"' + keyword + '\"' + "</h1>"
        suggestions = '<p><select name="dropdown">'
        for i in range(len(e.options)):
            suggestions = suggestions + "<option value ='" + e.options[i] + "'>" + e.options[i] + "</options>" 
        suggestions += "</select>"
        lengthPassed = '<p>Selected Length: <select name="lengthPassed">' + '<option value="' + length + '" selected>' + length + '</option></select>'
        form = '<form action=''/summarydrop method="POST">' + suggestions + lengthPassed + '<p><input type="submit" value="Submit"></form>' 
        output = title + form 
        return output
    else:
        return page


def getSearchList(keyword):
    return wk.search(keyword,suggestion=True)

def getPageTitle(keyword):
    return wk.title

def getPageUrl(keyword):
    return keyword.url

def getPageContent(keyword):
    return keyword.content

def getPageLinks(keyword):
    numberLinks = int(input("How many links do you want to see (minimum is 0)?")) 
    return keyword.links[numberLinks]

def setLang(language):
    return wk.set_lang(language)

def main():
    run(host = HOST, port=8080, debug=True)

if __name__ == "__main__":
    main()
