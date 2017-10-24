# import libraries
import urllib2
import clipboard
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://www.youtube.com/playlist?list=PLJNMX98vLTdQFfX-2uBjSCa4D8OYSyqtr'

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

myList = ""

# Take out the <div> of name and get its value
res = soup.find_all('a',{'class':'pl-video-title-link'})
for counter, l in enumerate(res):
    title = l.text.replace("'", r"\'").strip()
    ytId = l.get("href")[9:20]
    
    item = """
        $trailer%(counter)s = new SiteVideo([
            'site_id' => $siteId,
            'order' => 0,
            'title' => '%(title)s',
            'yt_id' => '%(ytId)s',
            'description' => '',
            'shareable_twitter' => true,
            'shareable_facebook' => true,
            'shareable_instagram' => true
        ]);
        $trailer%(counter)s->save();
    """ % locals()

    myList += item


clipboard.copy(myList)

