import requests
import time

# 使わなそう X-Api-Key
# BS4いらなくなる罠


def get_title_linkurl():
    base_url = (
        "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"  # 番号があるURL
    )
    res = requests.get(base_url)  # 番号を取得
    dic = res.json()  # 番号を辞書化

    numbers = []  # 空のリストを作成
    for number in range(0, 50):  # 番号を50回取得
        numbers.append(dic[number])
    return numbers


def get_info(numbers):  # 空のリストに入れる関数つくる  # get_infoあやしい
    for n in numbers:
        res = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{n}.json?print=pretty"
        )  # 取得した番号でURL作成し情報取得
        dic = res.json()  # 情報を辞書化
        title = dic["title"]  

        if "url" in dic:
            url = dic["url"]
            print(f"'title': '{title}', 'link': '{url}'")

        else:
            print(f"'title': {title}")

        time.sleep(1)  # ここで1秒止まる


def main():

    numbers = get_title_linkurl()
    get_info(numbers)


if __name__ == "__main__":
    main()
