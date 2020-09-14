import re
import random

# log/cups/access_log -> log/cups/
def get_path_part(filename):
    if filename[len(filename) - 1] == '/':
        return filename

    try:
        index = filename.rindex('/')
        dir_name = filename[0: index + 1]
        return dir_name
    except:
        return ''

# log/cups/access_log -> access_log
def get_filename_part(filename):
    try:
        pos = filename.rindex('/')
        base_name = filename[pos + 1:]
        return base_name
    except:
        return filename



# assets/image.png -> png
def get_file_extension(filename):
    try:
        occurrences = [m.start() for m in re.finditer('\.', filename)]
        return filename[occurrences[-1] + 1:]
    except:
        pass

    return ''


assert(get_path_part("log/cups/access_log") == "log/cups/")
assert(get_path_part("log/cups/") == "log/cups/")
assert(get_path_part("cups/access_log") == "cups/")
assert(get_path_part("access_log") == "")
assert(get_filename_part("log/cups/access_log") == "access_log")
assert(get_filename_part("log/cups/") == "")
assert(get_filename_part("cups/access_log") == "access_log")
assert(get_filename_part("access_log") == "access_log")
assert(get_file_extension("log/cups/access_log") == "")
assert(get_file_extension("base/FileHelper.cpp") == "cpp")
assert(get_file_extension("base/FileHelper.cpp.bak") == "bak")