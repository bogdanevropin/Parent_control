import os
import glob

current_directory = os.getcwd()

def file_cleaner(mask):
    #cleaning unnecessary files by type and ending patern of name (mask)
    # mask_dns_cmd = '\\*_dns.cmd'
    # mask_dns_txt = '\\*_dns.txt'
    # mask_urls_txt = '\\*_urls.txt'

    current_directory = os.getcwd()
    source_dir = current_directory  + mask

    for _file in glob.glob(source_dir):
        os.remove(_file)