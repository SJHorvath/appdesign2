import sys, re, os, urllib2



def dlfile(url):
    # Open the url
    try:
        f = urllib2.urlopen(url)
        print "downloading " + url

        # Open our local file for writing
        with open(os.path.basename(url), "wb") as local_file:
            local_file.write(f.read())

    #handle errors
    except urllib2.HTTPError, e:
        print "HTTP Error:", e.code, url
    except urllib2.URLError, e:
        print "URL Error:", e.reason, url

def imgextract(url):
  url_file = urllib2.urlopen(url)
	url_text = url_file.read()
	results = re.findall("<img.*?src=[\"'](.+?)[\"'].*?>", url_text)
	for result in results:
		dlfile(url)	

arg1 = sys.argv[1]

imgextract(arg1)