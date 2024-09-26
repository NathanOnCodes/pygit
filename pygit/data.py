import os


GIT_DIR = '.pygit'

def init():
    if not os.path.exists(GIT_DIR):
        os.mkdir(GIT_DIR)