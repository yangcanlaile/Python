#XPath 进行html信息抽取
from lxml import etree
def parseHTML():
    text ="""
    <div>
        <ul>
            <li class="item-0"><a href="link1.html">first item</a> </li>
            <li class="item-1"><a href="link2.html">second item</a> </li>
            <li class="item-inactive"><a href="link3.html">third item</a> </li>
            <li class="item-1"><a href="link4.html">fourth item</a> </li>
            <li class="item-0"><a href="link5.html">fifth item</a> </li>
        </ul>
    </div>
    
    """
    html = etree.HTML(text)
    #返回
    result = etree.tostring(html)
    print(type(result))
    print(result.decode('utf-8'))

#选取所有符合要求的节点
# //* 用于获取子孙节点
# /* 用于获取直接子节点
def selectAllElem():
    html = etree.parse('./test.html', etree.HTMLParser())
    result = html.xpath('//*')
    print(result)

#选中href属性的link4.html的a节点
def selectClass():
    html = etree.parse('./test.html', etree.HTMLParser())
    #选中href属性
    result = html.xpath('//a[@href="link4.html"]/../@class')
    #选中/ text()
    result = html.xpath('//li[@class="item-0"]/a/text()')
    #选中// text()
    result = html.xpath('//li[@class="item-0"]//text()')
    #选中 contains 包含li
    result = html.xpath('//li[contains(@class, "li")]/a/text()')
    print(result)
selectClass()