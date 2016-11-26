import datetime
import os
import platform
import time

def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime

def show_file_time(file):
    t = os.path.getmtime(file)
    print datetime.datetime.fromtimestamp(t)
    print "last modified: %s" % time.ctime(os.path.getmtime(file))
    print "created: %s" % time.ctime(os.path.getctime(file))
    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file)
    print "last modified: %s" % time.ctime(mtime)
    print "created: %s" % time.ctime(ctime)

    print os.stat(file).st_mtime      # time of most recent content modification,
    print os.stat(file).st_ctime      # platform dependent; time of most recent metadata change on Unix, or the time of creation on Windows)

def main():
    show_file_time('file_time.py')

if __name__ == '__main__':
    main()