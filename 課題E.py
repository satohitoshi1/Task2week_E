import requests
import time

# 使わなそう ❍❍ = {"X-Api-Key": "634d2f44705342cd9008bf457693044b"}
# API使うと記事番号で取得できる？(BS4いらなくなる罠まじでスパルタワロタ)


def get_title_link_url():
    base_url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
    res = requests.get(base_url)
    dic = res.json()  # 記事番号を辞書化

    numbers = []
    for number in range(0, 30):
        numbers.append(dic[number])   # 記事番号を30回取得

    return numbers


def get_info(number):

    for r in number:
        article_number = r
        response = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{article_number}.json?print=pretty"
        )

        dic = response.json()  # パース
        # print(dic)

        title = dic["title"]

        if "url" in dic:
            url = dic["url"]
            print(f"'title': '{title}', 'link': '{url}'")

        else:
            print(f"'title': {title}")

        time.sleep(1)  # 1秒


def main():

    numbers = get_title_link_url()
    get_info(numbers)


if __name__ == "__main__":
    main()
