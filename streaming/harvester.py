#!/usr/bin/env python
"""
Twitter Streaming API Harvester

Saves the stream of status JSON documents to
an archive file.

Author: Joshua Roesslein
License: MIT
Requires: Tweepy
"""

from optparse import OptionParser
from sys import exit
from tweepy import Stream, StreamListener


class HarvesterListener(StreamListener):

    def __init__(self, dest_file):
        StreamListener.__init__(self)
        self.file = open(dest_file, 'ab')

    def on_data(self, data):
        self.file.write(data)


def main(options, args):

    listener = HarvesterListener(options.file)

    try:
        username, password = args[0], args[1]
    except IndexError:
        print 'Missing username/password!'
        exit(1)

    stream = Stream(username, password, listener)

    try:
        stream.sample()
    except KeyboardInterrupt:
        exit(0)

 
if __name__ == '__main__':

    opt = OptionParser(
        description='Twitter Streaming API harvester',
		usage='harvester [options] <username> <password>'
    )
    opt.add_option('-f', '--file', dest='file', default='output.json',
		help='file to write statuses into')

    options, args = opt.parse_args()
    main(options, args)

