import alfredxml
import urllib
def query(arg):
    arg = arg.strip()
    if(len(arg)==0):
        rowList = [{'uid':'1',
                    'arg':'',
                    'autocomplete':'',
                    'icon':'head_1.png',
                    'subtitle':'Please Input' + arg,
                    'title':'Please Inputs'}];

        element = alfredxml.genAlfredXML(rowList)
        print(element)
        return
    else: 
        try:
            resp = urllib.urlopen("http://tip.mi.com/article")
        except Exception, info:
            rowList = [{'uid':'1',
                    'arg':'',
                    'autocomplete':'',
                    'icon':'head_1.png',
                    'subtitle':'there is sth wrong',
                    'title':'Sorry'}];

            element = alfredxml.genAlfredXML(rowList)
            print(info)
        else:
            rssContent = resp.read().encode("utf-8")
            print rssContent
            


        
