import re

def regular_exp(s):
    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)
    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '_', s)

    return s


def if_dir(parent_dir):
    if parent_dir is None:
        print('\nPlease enter the directory for download:')
        print("e.g: /home/user/manga\nPlease don't use back slash in the end. \n")
        parent_dir = input('Enter directory:')

    return parent_dir


def help():
    print("\n\n\tThe program is going to need user to specify their desired manga and specific path")
    print("\tfor it to download.")
    print("\tTo download manga, use -d or -D options.")
    print("\t     e.g.:")
    print("\t          python3 manga.py -D Yurukyan")
    print("\tFeel free to replace -D with -d or Yurukyan with the manga you like.")
    print("\t")
    print(" Options:")
    print("\t")
    print("\t-s   Search a manga and list it's available chapters.")
    print("\t-R   Re-download a chapter.")
    print("\t-d   Download specified range of chapters within the manga.")
    print("\t-D   Download all chapters available.\n\n")
