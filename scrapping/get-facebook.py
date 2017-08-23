import os

from time import sleep
from selenium import webdriver
from pathlib import Path

# Baixe o driver de https://sites.google.com/a/chromium.org/chromedriver/downloads
# e extraia o executável. Coloque na constante abaixo o caminho completo para ele.

DRIVER_PATH = r'{}/bin/chromedriver'.format(str(Path.home()))

WINDOW_WIDTH = 1024

WINDOW_HEIGHT = 768

SLEEP_TIME = 8

ROOT_NODE = 'pedrocunial'

DATA_FOLDER = 'facebook'


def scrape_nodes(browser):
    nodes = set()

    while True:
        added = False

        for element in browser.find_elements_by_css_selector(".fsl.fwb.fcb"):
            # try:
            a = element.find_element_by_tag_name('a')

            href = a.get_attribute('href')

            if ROOT_NODE in href:
                continue

            substring = href[25:(href.find('fref') - 1)]

            if substring.startswith('profile.php?id='):
                node = substring[15:]
            else:
                node = substring

            if node not in nodes:
                nodes.add(node)

                added = True
            if added:
                browser.execute_script(
                    'window.scrollTo(0, document.body.scrollHeight);')
                sleep(SLEEP_TIME)
            else:
                break

            # except selenium.common.exceptions.NoSuchElementException:
            #     pass



    return nodes


def save_successors(node, successors):
    path = os.path.join(DATA_FOLDER, node + '.txt')

    with open(path, 'w', encoding='utf-8') as file:
        for successor in successors:
            file.write(successor + '\n')


def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    browser = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)
    browser.set_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)

    browser.get('https://www.facebook.com')
    sleep(SLEEP_TIME)

    with open('{}/fb-keys.txt'.format(str(Path.home())), 'r') as f:
        uname = str(f.readline()).strip()
        pw = str(f.readline()).strip()

    browser.find_element_by_id('email').send_keys(uname)
    browser.find_element_by_id('pass').send_keys(pw)
    browser.find_element_by_id('loginbutton').click()
    sleep(SLEEP_TIME)

    browser.get('https://www.facebook.com/{}/friends'.format(ROOT_NODE))
    sleep(SLEEP_TIME)

    nodes = scrape_nodes(browser)

    save_successors(ROOT_NODE, nodes)

    for node in nodes:
        browser.get('https://www.facebook.com/{}/friends_mutual'.format(node))
        sleep(SLEEP_TIME)

        elements = browser.find_elements_by_class_name('_3sz')

        texts = [element.text for element in elements]

        if 'Amigos em comum' in texts:
            successors = scrape_nodes(browser)

            save_successors(node, successors)


if __name__ == '__main__':
    main()
