from mitmproxy import http
from mitmproxy.net.http import Headers
from mitmproxy import command
from mitmproxy import ctx
from mitmproxy import flow
import sys,os
import typing



class MyAddon:
    @command.command("myaddon.addheader")
    def addheader(self, flows: typing.Sequence[flow.Flow]) -> None:
        for f in flows:
            f.request.headers["Cache-Control"] = "no-cache"
        ctx.log.alert("done")


addons = [
    MyAddon()
]

def my_print(f_string):
    with open("/tmp/http_traffic",'a') as fp:
        fp.write(f_string+'\n')
    print(f_string)

#def request(flow: http.HTTPFlow):
#   my_print("http")
#   my_print(str(flow.request))


def response(flow: http.HTTPFlow):
    result = '\n' + '='*20+ 'request info:' + '='*20 + '\n\n'
    #print("FOR: " + flow.request.url)
    result += flow.request.method + " " + flow.request.url + " " + flow.request.http_version + '\n'
    result += '\n'+'-'*20 + 'request headers:' + '-'*20+'\n\n'
    for k, v in flow.request.headers.items():
        result += "%-20s: %s\n" % (k.upper(), v)

    result += '\n'+'-'*20 + 'response headers:'+'-'*20 +'\n\n'
    result += "%-20s: %s\n"%("STATUS CODE",str(flow.response.status_code))
    for k, v in flow.response.headers.items():
        result += "%-20s: %s\n" % (k.upper(), v)

    result += '\n'+'-'*20 + 'response content:' + '-'*20 + '\n\n'
    result += str(flow.response.content)
    my_print(result)
    return result
