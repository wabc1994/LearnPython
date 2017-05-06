from xml.dom.minidom import parse
import xml.dom.minidom
DOMTree=xml.dom.minidom.parse("tutorial.xml")
collection=DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print "Root element: %s "%collection.getAttribute("shelf")
movies=collection.getElementsByTagName("movie")
print movies
for movie in movies:
    print "***movie***"
    if movie.hasAttribute("title"):
        print "Title:%s"% movie.getAttribute("title")
    type=movie.getElementsByTagName('type')[0]
    print "Tpye:%s"%type.childNodes[0].data
    format1 = movie.getElementsByTagName('format')[0]
    print "Tpye:%s" % format1.childNodes[0].data
    rating= movie.getElementsByTagName('rating')[0]
    print "Tpye:%s" % rating.childNodes[0].data

