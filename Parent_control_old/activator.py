from clear import file_cleaner
import time

# cleaning unnecessary files by type and ending patern of name (mask):

# mask_dns_cmd => '\\*_dns.cmd'
# file_cleaner('\\*_dns.cmd')

# mask_dns_txt => '\\*_dns.txt'
# file_cleaner('\\*_dns.txt')

# mask_urls_txt => '\\*_urls.txt'
# file_cleaner('\\*_urls.txt')

from app_controller import apps_timer

# needs file controlled_exe_times.txt in this folder
# Sorted from top to bot by priority of control , example:
# chrome.exe: 11
# Taskmgr.exe: 2

from urls_controller import check_urls

# current urls from dns cash saved in text file with currrent time and _urls in the end

if __name__ == "__main__":

    apps_timer('controlled_exe_times.txt')
    file_cleaner('\\*_dns.cmd')
    check_urls()
    file_cleaner('\\*_dns.cmd')
    file_cleaner('\\*_dns.txt')
    time.sleep(10)
    file_cleaner('\\*_urls.txt')

