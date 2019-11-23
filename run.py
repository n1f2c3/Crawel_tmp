from optparse import OptionParser
import crawl

if __name__ == '__main__':
    optParser = OptionParser('-t <xxx.com >  -w <inurl: id>  --world <dictpatj> ')
    optParser.add_option("--world", "--word", action="store", type="string", default="test", dest="world"  ,help="zidian")
    optParser.add_option("-w", "--wordlist", action="store", type="string",default="dict_#", dest="wordlist",help="danci")
    optParser.add_option("-t", "--tagerget", action="store", type="string", default="tagerget", dest="tagerget" ,help="mubiao")
    option, args = optParser.parse_args()
    if option.world!="test":
        a=crawl.baidudork(option.world)
    if option.wordlist!="dict_#":
        f=open(option.wordlist,"r",encoding='utf-8')
        op=f.readlines()
        f.close()
        for i in op:
            if i[0:1]=="#":
                pass
            else:
                a=crawl.baidudork("site:"+option.tagerget+"  "+i)
                a.crawler()
    if option.wordlist == "dict_#":
        f = open(option.wordlist, "r",encoding='utf-8')
        op = f.readlines()
        f.close()
        for i in op:
            if i[0:1] == "#":
                pass
            else:
                a = crawl.baidudork("site:" + option.tagerget + "  " + i)
                print("site:" + option.tagerget + "  " + i)
                a.crawler()
