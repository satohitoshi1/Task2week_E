import bs4
import requests
import time

headers = {"X-Api-Key": "634d2f44705342cd9008bf457693044b"}

def get_title_link_url():
    base_url = "https://news.ycombinator.com/"
    res = requests.get(base_url)
    soup = bs4.BeautifulSoup(res.content, "html.parser")
    recipe_previews = soup.find_all(class_="ating")

    for recipe_preview in recipe_previews:
        a_tag = recipe_preview.find(class_="titlelink")
        print(a_tag)
        # recipes.append(
        # {"title": a_tag.text, "url": f"{base_url}{a_tag.attrs['href']}"}
        # urljoinで「/」の有無を気にせず連結できる(URLの場合)
        # {"title": a_tag.text, "url": urljoin(res.url, a_tag.attrs["href"])}


#    return recipes


# def main():
#     food = "トマト"
#
#     recipes = get_title_link_url_link_url(food)
#
#     for recipe in recipes:
#         print(f'レシピ名 {recipe["title"]}, URL {recipe["url"]}')

# for i in range(10):
#     time.sleep(1)  # ここで1秒止まる
#     print(i)
