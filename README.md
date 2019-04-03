# Mechanical keyboard all the things

Things I forgot that are nice:

* JS render / lua scripts: https://github.com/scrapy-plugins/scrapy-splash
* Item exporters: https://docs.scrapy.org/en/latest/topics/exporters.html
* Spider has a telnet console: https://docs.scrapy.org/en/latest/topics/telnetconsole.html
* You can run an spider as a service: https://github.com/scrapy-plugins/scrapy-jsonrpc. With that, you can query this service and the spider will run on demand.

This is the most expensive one: https://mechanicalkeyboards.com/shop/index.php?l=product_detail&p=4260, it looks very cool!

## Usage

```
scrapy crawl mechanicalkeyboards -a test_spider=1
scrapy crawl mechanicalkeyboards -o items.jl
```

Note you can also say items.csv, or items.json. Or use actual exporters: https://docs.scrapy.org/en/latest/topics/feed-exports.html

You can even store things on s3 or ftp :).

### mitmproxy

```
mitmproxy -p 9090
HTTPS_PROXY=http://localhost:9090 HTTP_PROXY=http://localhost:9090 scrapy crawl mechanicalkeyboards -o items.jl
```
