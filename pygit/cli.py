import argparse
import os
from . import data

def main():
    args = parse_args()
    args.func(args)


def parse_args():
    parser = argparse.ArgumentParser()

    commands = parser.add_subparsers(dest='command')
    commands.required = True

    init_parser = commands.add_parser('init')
    init_parser.set_defaults(func=init)


def init(args):
    data.init()
    print('Initialized empty ugit repository in %s' % os.path.join(os.getcwd(), data.GIT_DIR))