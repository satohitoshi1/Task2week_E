import requests
import time

# 使わなそう ❍❍ = {"X-Api-Key": "634d2f44705342cd9008bf457693044b"}
# BS4いらなくなる罠


def get_title_link_url():
    base_url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
    res = requests.get(base_url)
    dic = res.json()  # 番号を辞書化
    numbers = []
    for number in range(0, 50):  # 番号を50回取得
        numbers.append(dic[number])
    return numbers


def get_info(numbers):
    for n in numbers:
        res = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{n}.json?print=pretty"
        )
        dic = res.json()
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
