import os
import glob


def file_cleaner(mask, subfolder):
    # cleaning unnecessary files in subfolder by type and ending pattern of name (mask)
    # For clearing:
    # raw data:
    # subfolder = "\\raw_data"
    # type -> mask
    # dns command files mask-> '\\*_dns.cmd'
    # dns apps files-> '\\*_dns.txt'
    # for cleaning urls:
    # subfolder = "\\urls"
    # urls apps files mask -> '\\*_urls.txt'
    # for cleaning stopped_by:
    # subfolder = "\\stopped_by"
    # _stop txt files mask -> '\\*_stop.txt'

    current_directory = os.getcwd()
    cleaning_dir = current_directory + subfolder + mask
    
    # removing files by type in  subfolder
    for _file in glob.glob(cleaning_dir):
        os.remove(_file)
        