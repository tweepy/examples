"""
Twitter Streaming API Harvester

Saves the stream of status JSON documents to
an archive file.

Author: Joshua Roesslein
License: MIT
Requires: Tweepy
"""

from optparse import OptionParser
from tweepy import Stream, StreamListener


class HarvesterListener(StreamListener):

    def on_data(self, data):
        # TODO: write data to file
        return


def main(options, args):

    print 'Nothing to see here yet!'

    
if __name__ == '__main__':

    opt = OptionParser(
        description='Twitter Streaming API harvester'
    )
    opt.add_option('-i', '--interval', type='int', dest='interval', default=3600, help='Interval in seconds to split files')

    options, args = opt.parse_args()
    main(options, args)

