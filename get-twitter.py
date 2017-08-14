import os
import twitter

from twitter.error import TwitterError
from pathlib import Path

ROOT_NODE = 'realDonaldTrump'

DATA_FOLDER = 'twitter'


def build_path(node):
    return os.path.join(DATA_FOLDER, node + '.txt')


def main():
    home = str(Path.home())
    try:
        with open('/{}/twitter-keys.txt'.format(home), 'r') as f:
            CONSUMER_KEY = str(f.readline()).strip()
            CONSUMER_SECRET = str(f.readline()).strip()
            ACCESS_TOKEN_KEY = str(f.readline()).strip()
            ACCESS_TOKEN_SECRET = str(f.readline()).strip()

            api = twitter.Api(consumer_key=CONSUMER_KEY,
                              consumer_secret=CONSUMER_SECRET,
                              access_token_key=ACCESS_TOKEN_KEY,
                              access_token_secret=ACCESS_TOKEN_SECRET)
            print('AUTH SUCCESS')

    except:
        print('AUTH FAILED')
        api = twitter.Api()

    root_path = build_path(ROOT_NODE)

    with open(root_path, 'w', encoding='utf-8') as root_file:
        root_data = api.GetFriends(screen_name=ROOT_NODE)

        for root_subdata in root_data:
            node = root_subdata.screen_name

            print(node)

            try:
                data = api.GetFriends(screen_name=node)
            except TwitterError:
                continue

            root_file.write(node + '\n')

            path = build_path(node)

            with open(path, 'w', encoding='utf-8') as file:
                for subdata in data:
                    file.write(subdata.screen_name + '\n')


if __name__ == '__main__':
    main()
