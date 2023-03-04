import json
import requests
from bs4 import BeautifulSoup
import openai
from docx import Document
from docx.shared import Pt
from htmldocx import HtmlToDocx
import os


articleslist = []
OPENAI_API_KEY = "..."
openai.api_key = OPENAI_API_KEY
model_engine = "text-davinci-003"



with open('Results.json', 'r') as f:
  data = json.load(f)


for item in data:
    index = data.index(item) + 1
    print("Getting article", str(index))
    Title = item["Page"]
    Date = item["Date"]
    Summary = item["Excerpt"]
    Link = item["URL"]
    Source = item["Website"]
    res = requests.get(Link)
    soup = BeautifulSoup(res.content, "html.parser")
    try:
        Article = soup.article.text.strip()
    except:
        Article = soup.text.strip()
    articleslist.append([Title,Date,Summary,Link, Article,Source])



print("There are", str(len(articleslist)), "articles for summarising.")
for item in articleslist:
    index = articleslist.index(item) + 1
    print("Summarising article", str(index))
    prompt = "Can you summarise this article in five bullet points? An excerpt of the article is: " + item[2] + ". The article is: " + item[3]    
    accept = "N"
    while accept == "N":
        response = openai.Completion.create(engine=model_engine, prompt=prompt, temperature=0, max_tokens=1166)
        text = response.choices[0]["text"]
        print(item[0], "\n\n", text, "\n\n")
        accept = input("Do you want to accept summary?(Y/N)")
    item.append(text)


newsletter = ""

for i in articleslist:
    Headline = "<h2 style=\"font-size:20px\">" + i[0] + "</h2>"
    Date = "<p>" + i[1]
    Link = "<p>" + "URL: " + i[3]
    text = i[6].split(u'\u2022')
    bulletpointlist = "<ul>"
    for item in text:
        bulletpointlist = bulletpointlist + "<li>" + item + "</li>"
    bulletpointlist = bulletpointlist + "</ul>"
    source = "<p>" + "Source:" + i[5]
    newsletter = newsletter + Headline + Link + bulletpointlist + source


newsletter = newsletter + "</body></html>"

f = open("newsletter_intro.htm","r")
intro = f.read()
newsletter = intro + newsletter

document = Document()
new_parser = HtmlToDocx()
new_parser.add_html_to_document(newsletter, document)

document.save("newsletter.docx")




