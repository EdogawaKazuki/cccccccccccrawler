import scrapy
import traceback
from hpoi.items import MetaDataItem


class Spider(scrapy.Spider):
    name = "hpoi"

    def start_requests(self):
        urls = []
        for i in range(30000, 30010):
            urls.append('https://www.hpoi.net/hobby/' + str(i))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        meta_data_item = self.create_meta_data_item(response)
        f = open(response.url[-2:] + '.txt', 'w', encoding='utf8')
        f.write(str(meta_data_item))

    def create_meta_data_item(self, response):
        meta_data_item = MetaDataItem()
        meta_data_item['link'] = response.url
        meta_data_item['title'] = response.css('title::text').get()
        meta_data_item['item_type'] = '手办'
        intro_title = response.xpath("//div[@class='detail-content']/p/strong/text()")
        intro_content = response.xpath("//div[@class='detail-content']/p/text()").getall()
        intro_content += response.xpath("//div[@class='detail-content']/ul/li/text()").getall()
        meta_data_item['intro'] = {'title': intro_title, 'content': intro_content}
        attr_list = response.xpath("(//table[contains(@class,'info-box')])[1]/tbody/tr")
        attr_dict = {}
        for attr_pair in attr_list:
            try:
                title = attr_pair.xpath("./td")[0].xpath('./text()').get()
                content_temp = attr_pair.xpath("./td")[1].xpath('.//text()').getall()
                content = []
                for ele in content_temp:
                    if len(ele.replace('\r', '').replace('\n', '').replace(' ', '')):
                        content.append(ele.replace('\r', '').replace('\n', '').strip())
                attr_dict[title] = content
            except Exception:
                traceback.print_exc()
        meta_data_item['attribute'] = attr_dict
        return meta_data_item
