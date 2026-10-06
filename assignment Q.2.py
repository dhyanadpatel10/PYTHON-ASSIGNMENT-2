import re
import os

def parse_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Regex patterns for product name, price, rating
    names = re.findall(r'<h2 class="name">(.*?)</h2>', content)
    prices = re.findall(r'<span class="price">₹(\d+)</span>', content)
    ratings = re.findall(r'<span class="rating">([\d.]+)</span>', content)

    products = []
    for n, p, r in zip(names, prices, ratings):
        products.append((n.strip(), int(p), float(r)))
    return products


def rank_products(file_list, k):
    product_dict = {}

    for file in file_list:
        products = parse_html(file)
        for name, price, rating in products:
            if name not in product_dict:
                product_dict[name] = (price, rating)
            else:
                # Keep lowest price and highest rating
                old_price, old_rating = product_dict[name]
                product_dict[name] = (min(price, old_price), max(rating, old_rating))

    ranked = sorted(product_dict.items(), key=lambda x: (-x[1][1], x[1][0], x[0]))
    for name, (price, rating) in ranked[:k]:
        print(name, price, rating)


# ---------------- SAMPLE INPUT ----------------
# Suppose we have two HTML files: pageA.html and pageB.html
# pageA.html contains:
# <h2 class="name">Laptop Pro</h2><span class="price">₹55000</span><span class="rating">4.6</span>
# <h2 class="name">Wireless Mouse</h2><span class="price">₹799</span><span class="rating">4.4</span>
#
# pageB.html contains:
# <h2 class="name">Laptop Pro</h2><span class="price">₹53000</span><span class="rating">4.7</span>
# <h2 class="name">Mechanical Keyboard</h2><span class="price">₹2999</span><span class="rating">4.8</span>

rank_products(["pageA.html", "pageB.html"], k=2)
