import re

with open("twitters.txt", "r") as file:
    for line in file.readlines():
        pattern = r"kdt=([a-zA-Z0-9_]+); auth_token=([a-zA-Z0-9]+); ct0=([a-zA-Z0-9]+); twid=u=([0-9]+)"

        match = re.search(pattern, line)
        if match:
            kdt = match.group(1)
            auth_token = match.group(2)
            ct0 = match.group(3)
            twid = match.group(4)

        js_cookies = f'{{"name":"kdt","value":"{kdt}","domain":".twitter.com","path":"/","httpOnly":true,"secure":true,"session":true,"expires":1711992709,"sameSite":"unspecified"}},' \
                     f'{{"name":"auth_token","value":"{auth_token}","domain":".twitter.com","path":"/","httpOnly":true,"secure":true,"session":true,"expires":1711992709,"sameSite":"no_restriction"}},' \
                     f'{{"name":"ct0","value":"{ct0}","domain":".twitter.com","path":"/","httpOnly":false,"secure":true,"session":true,"expires":1711992709,"sameSite":"lax"}},' \
                     f'{{"name":"twid","value":"u%{twid}","domain":".twitter.com","path":"/","httpOnly":false,"secure":true,"session":true,"expires":1711992709,"sameSite":"no_restriction"}},' \
                     f'{{"name":"lang","value":"en","domain":"twitter.com","path":"/","httpOnly":false,"secure":false,"session":true,"expires":1711992709,"sameSite":"unspecified"}},' \
                     f'{{"name":"lang","value":"en","domain":"api.twitter.com","path":"/","httpOnly":false,"secure":false,"session":true,"expires":1711992709,"sameSite":"unspecified"}}'

        print(js_cookies)
