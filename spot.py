import urllib2
import json
import optparse

SEARCH_URL = 'http://ws.spotify.com/search/1/%s.json?q=%s'

def fetch_url(url):
    result = urllib2.urlopen(url).read()
    return json.loads(result)

def main(opts, args):
    url = SEARCH_URL % (opts.type, args[0])
    js = fetch_url(url)
    if opts.verbose:
        print js
    for item in js[opts.type+'s']:
        print item['name']

if __name__=='__main__':
    parser = optparse.OptionParser()
    parser.add_option('-t', '--type', dest='type', choices=('album', 'artist', 'track'), default='artist')
    parser.add_option('-v', '--verbose', action='store_true', dest='verbose', default=False)
    opts, args = parser.parse_args()
    main(opts, args)
