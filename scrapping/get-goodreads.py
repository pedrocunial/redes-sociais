import os

from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


# Baixe o driver de https://sites.google.com/a/chromium.org/chromedriver/downloads
# e extraia o executável. Coloque na constante abaixo o caminho completo para ele.

DRIVER_PATH = r'/caminho/para/o/executavel/do/driver'

WINDOW_WIDTH = 1024

WINDOW_HEIGHT = 768

SLEEP_TIME = 2

ROOT_NODE = '656983'

PAGE_LIMIT = 10

DATA_FOLDER = 'goodreads'


def scrape_nodes(browser, limit=None):
    nodes = []

    count = 0

    while True:
        try:
            element = browser.find_element_by_id('friendTable')
        except NoSuchElementException:
            return None

        for a in element.find_elements_by_tag_name('a'):
            if a.get_attribute('rel') == 'acquaintance':
                href = a.get_attribute('href')

                substring = href[26:]

                if substring.startswith('user'):
                    nodes.append(substring[10:substring.find('-')])

        if limit is not None:
            count += 1

            if count == limit:
                break

        try:
            element = browser.find_element_by_class_name('next_page')
        except NoSuchElementException:
            break

        if element.tag_name == 'a':
            browser.find_element_by_class_name('next_page').click()
            sleep(SLEEP_TIME)
        else:
            break

    return nodes


def build_path(node):
    return os.path.join(DATA_FOLDER, node + '.txt')


def main():
    browser = webdriver.Chrome(executable_path=DRIVER_PATH)
    browser.set_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)

    browser.get('https://www.goodreads.com/author_followings?id=' + ROOT_NODE)
    sleep(SLEEP_TIME)

    browser.find_element_by_css_selector('.gr-button.gr-button--dark').click()
    sleep(SLEEP_TIME)

    browser.find_element_by_id('user_email').send_keys('SEU LOGIN')
    browser.find_element_by_id('user_password').send_keys('SUA SENHA')
    browser.find_element_by_css_selector('.gr-button.gr-button--large').click()
    sleep(SLEEP_TIME)

    nodes = scrape_nodes(browser, PAGE_LIMIT)

    root_path = build_path(ROOT_NODE)

    with open(root_path, 'w', encoding='utf-8') as root_file:
        for node in nodes:
            browser.get('https://www.goodreads.com/friend/user/' + node)
            sleep(SLEEP_TIME)

            successors = scrape_nodes(browser)

            if successors is not None:
                root_file.write(node + '\n')

                path = build_path(node)

                with open(path, 'w', encoding='utf-8') as file:
                    for successor in successors:
                        file.write(successor + '\n')


if __name__ == '__main__':
    main()
