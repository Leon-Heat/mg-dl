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

    parent_dir = None   # Change None into that directory if wanted, e.g.: '/home/kaze/pic/manga'
                        # Make sure you have surround it with quotation marks and please don't add
                        # any slashes in the end of your directory. 


    for opt, arg in options:
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
            parent_dir = if_dir(parent_dir)
            num_request_download(arg, n, parent_dir)
        if opt in ('-D', '--download-all'):
            profile()
            on_and_search(arg)
            n = list_names()
            parent_dir = if_dir(parent_dir)
            download(arg, 1, n, parent_dir)

opt()

