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

fp = open("/tmp/http_traffic",'w')

addons = [
    MyAddon()
]

def my_print(f_string):
    fp.write(f_string+'\n')
    print(f_string)

#def request(flow: http.HTTPFlow):
#   my_print("http")
#   my_print(str(flow.request))


def response(flow: http.HTTPFlow):
    my_print("\n")
    my_print("="*50)
    #print("FOR: " + flow.request.url)
    my_print(flow.request.method + " " + flow.request.path + " " + flow.request.http_version)

    my_print("-"*50 + "request headers:")
    for k, v in flow.request.headers.items():
        my_print("%-20s: %s" % (k.upper(), v))

    my_print("-"*50 + "response headers:")
    for k, v in flow.response.headers.items():
        my_print("%-20s: %s" % (k.upper(), v))
    my_print(str(flow.response.content))
