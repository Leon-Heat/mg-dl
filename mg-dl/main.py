from lib import *

def opt():  #  Dectect Options

#  The program is going to need user to specify their desired manga and specific path
#  for it to download.
#  To download manga, use -d or -D options.
#       e.g.:
#            python3 manga.py -D Yurukyan
#  Feel free to replace -D with -d or Yurukyan with the manga you like.

# Options:

#  -s   Search a manga and list it's available chapters.
#  -R   Re-download a chapter.
#  -d   Download specified range of chapters within the manga.
#  -D   Download all chapters available.

    options, remainder = getopt.gnu_getopt(sys.argv[1:], 's:d:D:h', ['search', 
                                                                    'download',
                                                                    'download-all',
                                                                    'help'])


    for opt, arg in options:
        print(arg, remainder)

        for element in remainder:
            arg += str(' %s' % element)
            manga = (regular_exp(arg))


        if opt in ('-h', '--help'):
            help() 
            break

        if opt in ('-s', '--search'):
            profile()
            on_and_search(arg)
            list_names()

        if opt in ('-d', '--download'):
            profile()
            on_and_search(arg)
            n = list_names()
            Manga.parent_dir = if_dir(Manga.parent_dir)
            num_request_download(arg, n, Manga.parent_dir)

        if opt in ('-D', '--download-all'):
            profile()
            on_and_search(manga)
            n = list_names()
            Manga.parent_dir = if_dir(Manga.parent_dir)
            download(arg, 1, n, Manga.parent_dir)

config = ['directory=*']
Manga.parent_dir = read_config(config[0])
opt()
#implement a file variable
#implement a better way to search mangas
