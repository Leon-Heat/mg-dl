from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import staleness_of
from utils import *

import time, os, wget, getopt, sys

class Manga():
    driver = None
    parent_dir = None

def profile():  # Setting up profile for driver
    profile = webdriver.FirefoxProfile()
    profile.set_preference('places.history.enabled', False )
    profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', False)
    profile.set_preference('javascript.enabled', False )
    Manga.driver = webdriver.Firefox(firefox_profile = profile)


def on_and_search(key):  # Search the manga and access to the page that contains list of chapters.
    print('Searching manga....')
    Manga.driver.get('https://kissmanga.com/Manga/%s' % key)
    wait_and_click(30, '//tr//td//a[contains(@href, "/Manga/")]')
    wait(20, '//select[contains(@class, "selectChapter")]', 'presence')


def list_init():  # Statements for creating a list.
    print('Getting list of chapters....')
    global s_elem, name_list, name
    s_elem = Manga.driver.find_element_by_xpath('//select[contains(@class, "selectChapter")]')
    name_list = s_elem.find_elements_by_tag_name('option')
    name = []


def list_names():  # Trasfer chapter's names into a list
    list_init()
    x = 0

    for l in name_list:
        x += 1
        name.append(l.text)
        print(x, name[x-1])

    print('Total: %s chapters\n\n' % str(x))
    return str(x)


def num_request_download(key, string, parent_dir):
    print('Please enter 2 numbers that defines a range of chapters(1 - %s):' % string)
    print('e.g: 1 30')
    Min, Max = input("Enter values: ").split()

    download(key, Min, Max, parent_dir)


def download(key, Min, Max, parent_dir):  # This goes back to the previous page and downloads the manga on to the specified path.
    print(parent_dir)
    mkdir_parent(key, parent_dir)
    print('Range set between %s - %s.' %(Min, Max))

    x = 0
    for l in name_list:
        x += 1
        Manga.driver.get('https://kissmanga.com/Manga/%s' % key)
        wait_and_click(20, '//a[contains(text(), "%s")]' % name[x-1])
        path = '%s/%s/%d.%s' %(parent_dir, dir, x, regular_exp(name[x-1]))
        mkdir_chapter(path)
        fetch(path, name[x-1])


def fetch(path_dir, chapter):
    print('Downloading %s....' % chapter)
    wait(5, '//div[contains(@id, "divImage")]//p//img', 'presence')
    images = Manga.driver.find_elements_by_xpath('//div[contains(@id, "divImage")]//p//img')
    n = 0

    for image in images:
        n += 1
        os.system('wget -O %s/%d.jpg %s  >/dev/null 2>&1' %(path_dir, n, image.get_attribute('src')))


def mkdir_parent(key, parent_dir):
    global dir, path
    dir = key 
    path = '%s/%s' %(parent_dir, dir)
    os.system('mkdir -p %s' % path)
    print('\nDirectory "%s" has been created' % path) 

def mkdir_chapter(path_dir):
    os.system('mkdir -p %s' % path_dir)
    print('Directory "%s" has been created' % path_dir) 

def wait_and_click(time, string):  # Wait for an element to be usable and click
    Wait(Manga.driver, time).until(EC.element_to_be_clickable((By.XPATH, string)))
    link = Manga.driver.find_element_by_xpath(string)
    link.click()

def wait(time, string, mode):  # Wait for an element to be usable
    if mode == 'clickable':
        Wait(Manga.driver, time).until(EC.element_to_be_clickable((By.XPATH, string)))
    elif mode == 'presence':
        Wait(Manga.driver, time).until(EC.presence_of_element_located((By.XPATH, string)))

