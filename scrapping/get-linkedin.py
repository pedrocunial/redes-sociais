import os

from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException


# Baixe o driver de https://sites.google.com/a/chromium.org/chromedriver/downloads
# e extraia o executável. Coloque na constante abaixo o caminho completo para ele.

DRIVER_PATH = r'/caminho/para/o/executavel/do/driver'

WINDOW_WIDTH = 1024

WINDOW_HEIGHT = 768

SLEEP_TIME = 2

ROOT_NODE = 'SEU ID'

DATA_FOLDER = 'linkedin'


def scrape_nodes(browser, selector):
    nodes = set()

    while True:
        while True:
            added = False

            for element in browser.find_elements_by_css_selector(selector):
                href = element.get_attribute('href')

                node = href[28:-1]

                if node not in nodes:
                    nodes.add(node)

                    added = True

            if added:
                browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                sleep(SLEEP_TIME)
            else:
                break

        try:
            element = browser.find_element_by_class_name('next-text').click()
            sleep(SLEEP_TIME)
        except WebDriverException:
            break

    return nodes


def save_successors(node, successors):
    path = os.path.join(DATA_FOLDER, node + '.txt')

    with open(path, 'w', encoding='utf-8') as file:
        for successor in successors:
            file.write(successor + '\n')


def main():
    browser = webdriver.Chrome(executable_path=DRIVER_PATH)
    browser.set_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)

    browser.get('https://www.linkedin.com/mynetwork/invite-connect/connections')
    sleep(SLEEP_TIME)

    frames = browser.find_elements_by_tag_name('iframe')
    browser.switch_to_frame(frames[0])
    browser.find_element_by_class_name('sign-in-link').click()
    browser.switch_to_default_content()
    sleep(SLEEP_TIME)

    frames = browser.find_elements_by_tag_name('iframe')
    browser.switch_to_frame(frames[0])
    browser.find_element_by_id('session_key-login').send_keys('SEU LOGIN')
    browser.find_element_by_id('session_password-login').send_keys('SUA SENHA')
    browser.find_element_by_id('btn-primary').click()
    browser.switch_to_default_content()
    sleep(SLEEP_TIME)

    nodes = scrape_nodes(browser, '.mn-person-info__link.ember-view')

    save_successors(ROOT_NODE, nodes)

    for node in nodes:
        browser.get('https://www.linkedin.com/in/' + node)
        sleep(SLEEP_TIME)

        try:
            element = browser.find_element_by_id('highlights-container')
        except NoSuchElementException:
            continue

        for a in element.find_elements_by_tag_name('a'):
            h3 = a.find_element_by_tag_name('h3')

            if h3.text.endswith('conexões em comum'):
                browser.get(a.get_attribute('href'))
                sleep(SLEEP_TIME)

                successors = scrape_nodes(browser, '.search-result__result-link.ember-view')

                save_successors(node, successors)

                break


if __name__ == '__main__':
    main()
