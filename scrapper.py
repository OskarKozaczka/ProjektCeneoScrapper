#import bibliotek
import requests
from bs4 import BeautifulSoup
#adres URL strony z opiniami

url = "https://www.ceneo.pl/76891701#tab=reviews"

#pobieranie kodu strony html
page_response = requests.get(url)

page_tree = BeautifulSoup(page_response.text, "html.parser")





#wybranie z kodu strony fragmentów odpowiadających poszczególnym opiniom
opinions = page_tree.select("li.review-box")

#ekstrakcja składowych dla pierwszej opini z listy 


opinion=opinions[1]
opinion_id = opinion["data-entry-id"]
author = opinion.select("div.revier-name-line")
recomendation = opinion.select("div.product-review-summary > em")
stars = opinion.select("span.review-score-count")
purchased = opinion.select("div.product.review-pz")
useful= opinion.select("button.vote-yes")[0]["data-total-vote"]
useless = opinion.select("button.vote-no")[0]["data-total-vote"]

print(opinion)

# - opinia: li.review-box
# - identyfikator: li.review-box["data-entry-id"]
# - autor: div.revier-name-line
# - rekomendacja: div.product-review-summary > em
# - gwiazdki: span.review-score-count
# - potwierdzona zakupem: div.product.review-pz
# - data wystawienia: span.review-time > time["date-time"] - pierwszy element listy
# - data zakupu: span.review-time > time["date-time"] - drugi element listy
# - przydatna: button.vote-yes["data-total-vote"]
# - nieprzydatna: button.vote-no["data-total-vote"]
# - treść: p.product-review-body
# - wady: div.cons-cell > ul
# - zalety: div.pros-cell > ul