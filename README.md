# CeneoScraper11S
# Etap 1 - pobranie pojedynczeej opinii 
- opinia    : li.review-box
- identyfikator     : li.review-box[data-entry-id]
- autor     : div.reviewer-name-line
- rekomendacja      : div.product-review-summary > em
- liczba gwiazdek       : span.product.review.score-count
- czy potwierdzona zakupem      : div.product-review-pz
- data wystawienia      : span.product.review > time["datetime"] - pierwsze wystapienie
- data zakupu   : span.product.review > time["datetime"] - drugie wystapienie
- przydatna     : button.vote-yes["data.total-vote"]
- nieprzydatna      : button.vote-no["data.total-vote"]
- treść     : p.product-review-body
- wady      : div.cons-cell > ul
- zalety  :div.pros-cell > ul 
