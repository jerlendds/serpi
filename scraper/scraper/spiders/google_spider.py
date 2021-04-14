import scrapy

xpaths = {
    "results": [
        {
            "xpath": "/html/body/div[1]/div/div/div/a",
            "description": "amp google result header"
        },
        {
            "xpath": "/html/body/div/div/div/div/div/div/div/div/div",
            "description": "amp google result description area (can include rating, sublinks, etc)"
        }
    ],

}



class GoogleSpider(scrapy.Spider):
    name = 'google'
    starts_urls = [
            'https://www.google.com/search?q=hello+void&ampie=UTF-8&ampgbv=1&amp'
        ]

    def parse(self, response):
        pass

