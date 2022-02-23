# Download project euler problems, save as number for now....
import urllib.request
import time
n = 1
while n < 800:
    url = "https://projecteuler.net/problem={n}".format(n=n)
    fname = "problem_{n}.html".format(n=n)

    data_req = urllib.request.Request(url)
    # set a header for a cookie
    data_req.add_header("user-agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36, val)")
    data_req.add_header("Cookie", "<<SESSION>>")
    data = urllib.request.urlopen(data_req).read()
    # data = data_req.get_full_url() urlopen(url).read().decode('utf-8')
    with open(fname, "wb") as f:
        f.write(data)
    time.sleep(5)

    n+=1