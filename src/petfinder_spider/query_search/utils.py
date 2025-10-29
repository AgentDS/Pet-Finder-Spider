from pathlib import Path

from ..utils.paths import cache_path

HEADER_CACHE_FILE_PATH = cache_path('header_cache')

def load_request_header_string():
    # TODO: read header cache from HEADER_CACHE_FILE_PATH
    header = None
    return header


""" 
accept
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
accept-encoding
gzip, deflate, br, zstd
accept-language
en-US,en;q=0.9,zh-TW;q=0.8,zh-CN;q=0.7,zh;q=0.6
cache-control
no-cache
cookie
PFSESSION=9050e57feb584d5cd790aac8435e607c; G_ENABLED_IDPS=google; _cc_id=ba60d9890b152faa7f49be5651ef301d; panoramaId_expiry=1761942761159; panoramaId=09b6143da413e50dea4a9981be0c16d53938862915389d1c0f2f5e76b1a998d9; panoramaIdType=panoIndiv; _ga=GA1.1.1698904497.1761337961; _fbp=fb.1.1761337961490.787317122354796451; _cls_v=abc14a7c-e5ab-42ea-ae22-d69d4aebfb22; _cls_s=da44c52f-21a4-482b-bac8-35bd799588f2:0; impressions=2; impressions=3; profiles_uuid=b34790cf-310b-4e52-bba6-0d52620bb8f2; ab.storage.deviceId.844a5ca9-eecc-49f1-9abc-b1961d4e4953=%7B%22g%22%3A%22684a2f69-2c50-bc30-4712-2e06e1a3c115%22%2C%22c%22%3A1761337971507%2C%22l%22%3A1761454807532%7D; ab.storage.userId.844a5ca9-eecc-49f1-9abc-b1961d4e4953=%7B%22g%22%3A%22b34790cf-310b-4e52-bba6-0d52620bb8f2%22%2C%22c%22%3A1761454807531%2C%22l%22%3A1761454807532%7D; _fbc=fb.1.1761505340242.IwY2xjawNrT4lleHRuA2FlbQIxMABicmlkETFIbWxlelBKZE93N0xRb01lAR5D4gLXLZaK3ADe085NItldYNIRjddcsLhHMK3GbX84K0Mjqvy47ntfvORrZw_aem_jQgYFmpb6d0l5Yf4d_0bng; cto_bundle=Bk8wBl9ISlJpYUpLMXNlY296MFgzZlBaN1JjNXVlekJ5Z2NIV3pDMUlBYzJVcmVOZ2NwM3IlMkZrRm0lMkJhS1hsVEc3clZ0aHJudXRQVmNRWE9PYVhjR3pyS3FNYiUyRmZDakFhWndnc2VpNlpnbFlrSjU3a2I0YllWdW0zZHRPYTR2eEZsTzVkVSUyRkE4elI4SkpYekh2NzQ1bjUyckUxcjdaNTFYVktuUDlyMzBnVGJhRWtIZXRlY1BldHdKd1dYN3dEN2tDbVV4U3hwNGIzMlNuQTFuTGFtMWI0TUZZV0Uza0RwTW9GSzJZOGtxNjNRTWhrYzdpUjBaaCUyRmJuZ3l4elElMkZQYU8xWGlaWG5Qdm4lMkIwazY0ZTd3STZ0WUFCSDVRJTNEJTNE; recently_viewed_pets=%5B78882197%2C79015887%2C79002001%2C78932297%2C78956371%2C78147819%2C78770281%2C78894999%2C78953126%2C78723170%2C78003514%2C77260189%2C78932362%2C77435927%2C78934214%2C78690704%2C78936029%2C78936061%2C77772617%2C78450650%5D; last_pet_search=https%3A%2F%2Fwww.petfinder.com%2Fsearch%2Fcats-for-adoption%2Fus%2Ftn%2Fnashville%2F%3Fage%255B0%255D%3DBaby%26breed%255B0%255D%3DSiamese%26sort%255B0%255D%3Dbest_match%26o%3D14; __gads=ID=e996268f59c4b7ce:T=1761337960:RT=1761683816:S=ALNI_MZ1beYqkz2ziP464lU_TApR8Y1HwA; __eoi=ID=732b17145bc1c516:T=1761337961:RT=1761683816:S=AA-AfjbnrzTc_lB1X63D3SBbZQIG; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Oct+28+2025+16%3A39%3A08+GMT-0400+(Eastern+Daylight+Time)&version=202507.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CBG142%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false; user_location_slug=us/mi/lansing; _ga_LWVJC60CMJ=GS2.1.s1761677473$o11$g1$t1761683948$j60$l0$h0; ab.storage.sessionId.844a5ca9-eecc-49f1-9abc-b1961d4e4953=%7B%22g%22%3A%22a9c42535-5a23-2083-0ac7-35f2888d13b0%22%2C%22e%22%3A1761685749622%2C%22c%22%3A1761683200564%2C%22l%22%3A1761683949622%7D; _ga_5H1R91DP2Q=GS2.1.s1761677470$o11$g1$t1761683949$j45$l0$h0
dnt
1
pragma
no-cache
priority
u=0, i
referer
https://www.petfinder.com/cats-and-kittens/breeds/siamese/
sec-ch-ua
"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"
sec-ch-ua-mobile
?0
sec-ch-ua-platform
"macOS"
sec-fetch-dest
document
sec-fetch-mode
navigate
sec-fetch-site
same-origin
sec-fetch-user
?1
upgrade-insecure-requests
1
user-agent
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36
"""


"""
curl 'https://www.petfinder.com/search/cats-for-adoption/us/mi/lansing/?age%5B0%5D=Baby&breed%5B0%5D=Siamese&sort%5B0%5D=best_match' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'accept-language: en-US,en;q=0.9,zh-TW;q=0.8,zh-CN;q=0.7,zh;q=0.6' \
  -H 'cache-control: no-cache' \
  -b 'PFSESSION=9050e57feb584d5cd790aac8435e607c; G_ENABLED_IDPS=google; _cc_id=ba60d9890b152faa7f49be5651ef301d; panoramaId_expiry=1761942761159; panoramaId=09b6143da413e50dea4a9981be0c16d53938862915389d1c0f2f5e76b1a998d9; panoramaIdType=panoIndiv; _ga=GA1.1.1698904497.1761337961; _fbp=fb.1.1761337961490.787317122354796451; _cls_v=abc14a7c-e5ab-42ea-ae22-d69d4aebfb22; _cls_s=da44c52f-21a4-482b-bac8-35bd799588f2:0; impressions=2; impressions=3; profiles_uuid=b34790cf-310b-4e52-bba6-0d52620bb8f2; ab.storage.deviceId.844a5ca9-eecc-49f1-9abc-b1961d4e4953=%7B%22g%22%3A%22684a2f69-2c50-bc30-4712-2e06e1a3c115%22%2C%22c%22%3A1761337971507%2C%22l%22%3A1761454807532%7D; ab.storage.userId.844a5ca9-eecc-49f1-9abc-b1961d4e4953=%7B%22g%22%3A%22b34790cf-310b-4e52-bba6-0d52620bb8f2%22%2C%22c%22%3A1761454807531%2C%22l%22%3A1761454807532%7D; _fbc=fb.1.1761505340242.IwY2xjawNrT4lleHRuA2FlbQIxMABicmlkETFIbWxlelBKZE93N0xRb01lAR5D4gLXLZaK3ADe085NItldYNIRjddcsLhHMK3GbX84K0Mjqvy47ntfvORrZw_aem_jQgYFmpb6d0l5Yf4d_0bng; cto_bundle=Bk8wBl9ISlJpYUpLMXNlY296MFgzZlBaN1JjNXVlekJ5Z2NIV3pDMUlBYzJVcmVOZ2NwM3IlMkZrRm0lMkJhS1hsVEc3clZ0aHJudXRQVmNRWE9PYVhjR3pyS3FNYiUyRmZDakFhWndnc2VpNlpnbFlrSjU3a2I0YllWdW0zZHRPYTR2eEZsTzVkVSUyRkE4elI4SkpYekh2NzQ1bjUyckUxcjdaNTFYVktuUDlyMzBnVGJhRWtIZXRlY1BldHdKd1dYN3dEN2tDbVV4U3hwNGIzMlNuQTFuTGFtMWI0TUZZV0Uza0RwTW9GSzJZOGtxNjNRTWhrYzdpUjBaaCUyRmJuZ3l4elElMkZQYU8xWGlaWG5Qdm4lMkIwazY0ZTd3STZ0WUFCSDVRJTNEJTNE; recently_viewed_pets=%5B78882197%2C79015887%2C79002001%2C78932297%2C78956371%2C78147819%2C78770281%2C78894999%2C78953126%2C78723170%2C78003514%2C77260189%2C78932362%2C77435927%2C78934214%2C78690704%2C78936029%2C78936061%2C77772617%2C78450650%5D; last_pet_search=https%3A%2F%2Fwww.petfinder.com%2Fsearch%2Fcats-for-adoption%2Fus%2Ftn%2Fnashville%2F%3Fage%255B0%255D%3DBaby%26breed%255B0%255D%3DSiamese%26sort%255B0%255D%3Dbest_match%26o%3D14; __gads=ID=e996268f59c4b7ce:T=1761337960:RT=1761683816:S=ALNI_MZ1beYqkz2ziP464lU_TApR8Y1HwA; __eoi=ID=732b17145bc1c516:T=1761337961:RT=1761683816:S=AA-AfjbnrzTc_lB1X63D3SBbZQIG; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Oct+28+2025+16%3A39%3A08+GMT-0400+(Eastern+Daylight+Time)&version=202507.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CBG142%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false; user_location_slug=us/mi/lansing; _ga_LWVJC60CMJ=GS2.1.s1761677473$o11$g1$t1761683948$j60$l0$h0; ab.storage.sessionId.844a5ca9-eecc-49f1-9abc-b1961d4e4953=%7B%22g%22%3A%22a9c42535-5a23-2083-0ac7-35f2888d13b0%22%2C%22e%22%3A1761685749622%2C%22c%22%3A1761683200564%2C%22l%22%3A1761683949622%7D; _ga_5H1R91DP2Q=GS2.1.s1761677470$o11$g1$t1761683949$j45$l0$h0' \
  -H 'dnt: 1' \
  -H 'pragma: no-cache' \
  -H 'priority: u=0, i' \
  -H 'referer: https://www.petfinder.com/cats-and-kittens/breeds/siamese/' \
  -H 'sec-ch-ua: "Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-user: ?1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'
"""


'''
{
  "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9,zh-TW;q=0.8,zh-CN;q=0.7,zh;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "referrer": "https://www.petfinder.com/cats-and-kittens/breeds/siamese/",
    "cookie": ""PFSESSION=9050e57feb584d5cd790aac8435e607c; G_ENABLED_IDPS=google; _cc_id=ba60d9890b152faa7f49be5651ef301d; panoramaId_expiry=1761942761159; panoramaId=09b6143da413e50dea4a9981be0c16d53938862915389d1c0f2f5e76b1a998d9; panoramaIdType=panoIndiv; _ga=GA1.1.1698904497.1761337961; _fbp=fb.1.1761337961490.787317122354796451; _cls_v=abc14a7c-e5ab-42ea-ae22-d69d4aebfb22; _cls_s=da44c52f-21a4-482b-bac8-35bd799588f2:0; impressions=2; impressions=3; profiles_uuid=b34790cf-310b-4e52-bba6-0d52620bb8f2; ab.storage.deviceId.844a5ca9-eecc-49f1-9abc-b1961d4e4953=%7B%22g%22%3A%22684a2f69-2c50-bc30-4712-2e06e1a3c115%22%2C%22c%22%3A1761337971507%2C%22l%22%3A1761454807532%7D; ab.storage.userId.844a5ca9-eecc-49f1-9abc-b1961d4e4953=%7B%22g%22%3A%22b34790cf-310b-4e52-bba6-0d52620bb8f2%22%2C%22c%22%3A1761454807531%2C%22l%22%3A1761454807532%7D; _fbc=fb.1.1761505340242.IwY2xjawNrT4lleHRuA2FlbQIxMABicmlkETFIbWxlelBKZE93N0xRb01lAR5D4gLXLZaK3ADe085NItldYNIRjddcsLhHMK3GbX84K0Mjqvy47ntfvORrZw_aem_jQgYFmpb6d0l5Yf4d_0bng; cto_bundle=Bk8wBl9ISlJpYUpLMXNlY296MFgzZlBaN1JjNXVlekJ5Z2NIV3pDMUlBYzJVcmVOZ2NwM3IlMkZrRm0lMkJhS1hsVEc3clZ0aHJudXRQVmNRWE9PYVhjR3pyS3FNYiUyRmZDakFhWndnc2VpNlpnbFlrSjU3a2I0YllWdW0zZHRPYTR2eEZsTzVkVSUyRkE4elI4SkpYekh2NzQ1bjUyckUxcjdaNTFYVktuUDlyMzBnVGJhRWtIZXRlY1BldHdKd1dYN3dEN2tDbVV4U3hwNGIzMlNuQTFuTGFtMWI0TUZZV0Uza0RwTW9GSzJZOGtxNjNRTWhrYzdpUjBaaCUyRmJuZ3l4elElMkZQYU8xWGlaWG5Qdm4lMkIwazY0ZTd3STZ0WUFCSDVRJTNEJTNE; recently_viewed_pets=%5B78882197%2C79015887%2C79002001%2C78932297%2C78956371%2C78147819%2C78770281%2C78894999%2C78953126%2C78723170%2C78003514%2C77260189%2C78932362%2C77435927%2C78934214%2C78690704%2C78936029%2C78936061%2C77772617%2C78450650%5D; last_pet_search=https%3A%2F%2Fwww.petfinder.com%2Fsearch%2Fcats-for-adoption%2Fus%2Ftn%2Fnashville%2F%3Fage%255B0%255D%3DBaby%26breed%255B0%255D%3DSiamese%26sort%255B0%255D%3Dbest_match%26o%3D14; __gads=ID=e996268f59c4b7ce:T=1761337960:RT=1761683816:S=ALNI_MZ1beYqkz2ziP464lU_TApR8Y1HwA; __eoi=ID=732b17145bc1c516:T=1761337961:RT=1761683816:S=AA-AfjbnrzTc_lB1X63D3SBbZQIG; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Oct+28+2025+16%3A39%3A08+GMT-0400+(Eastern+Daylight+Time)&version=202507.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CBG142%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false; user_location_slug=us/mi/lansing; _ga_LWVJC60CMJ=GS2.1.s1761677473$o11$g1$t1761683948$j60$l0$h0; ab.storage.sessionId.844a5ca9-eecc-49f1-9abc-b1961d4e4953=%7B%22g%22%3A%22a9c42535-5a23-2083-0ac7-35f2888d13b0%22%2C%22e%22%3A1761685749622%2C%22c%22%3A1761683200564%2C%22l%22%3A1761683949622%7D; _ga_5H1R91DP2Q=GS2.1.s1761677470$o11$g1$t1761683949$j45$l0$h0"
  },
  
  "body": null,
  "method": "GET",
  "mode": "cors",
  "credentials": "include"
}
'''