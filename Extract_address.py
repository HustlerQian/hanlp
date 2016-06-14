#=-= coding:utf-8 =-=

import re

#地址的表达式pattern
Address_pattern= u'((/ns)+(/nz)?(/nt)?(/m(/q|/n))?)'

#建立地址字典
def make_address_dic(textlist):
    address_dic={}
    facetlist=u''
    wordindex=1
    facetindex=0
    for item in textlist:
        word,facet=item
        facetlist+=facet
        #已facetindex给每个标注的词当键值，保存词，词性，词在这句句子中的起始和终止位置
        address_dic[facetindex]={'word':word,'facet':facet,'wordstart':wordindex,'wordend':wordindex+len(word)-1}
        #print len(word)
        #index加上各自长度word/facet
        wordindex+=len(word)
        facetindex+=len(facet)
    return address_dic,facetlist


#主处理函数
def process(address_dic,facetlist):
    Address_location={}
    resultlist=re.compile(Address_pattern).findall(facetlist)
    #上一次裁剪掉的长度
    LastfacetLength=0
    for result in resultlist:
        
        resultStr=result[0]
        #记录正则匹配的结果在裁剪前的facetlist起始和终止位置
        stringstart,stringend=facetlist.find(resultStr)+LastfacetLength,facetlist.find(resultStr)+LastfacetLength+len(resultStr)-1
        #裁剪起始index
        CutStart=facetlist.find(resultStr)+len(resultStr)
        word=''
        wordstart=0
        for facetindex in sorted(address_dic.keys()):
            #根据facetlist位置将word拼接起来
            if facetindex>=stringstart and facetindex<=stringend:
                    wordlist=address_dic[facetindex]
                    #拼接词
                    word+=wordlist['word']
                    #记录词的起始
                    if wordstart==0:
                        wordstart=wordlist['wordstart']
                    #记录词的结束
                    wordend=wordlist['wordend']
        #print word
        #如果重复出现一个词，将位置添加在之后
        if not Address_location.has_key(word):
            Address_location[word]=[(wordstart,wordend)]
        else:
            Address_location[word].append((wordstart,wordend))
        #裁剪后的facetlist
        facetlist=facetlist[CutStart:]
        LastfacetLength+=CutStart
    return Address_location
    
    
    
def main():
    textlist=[(u'地址', u'/n'), (u'：', u'/w'), (u'上海市', u'/ns'), (u'杨浦区', u'/ns'), (u'四平路', u'/nz'), (u'1239号同济大学', u'/nt'), (u'，', u'/w'), (u'电话', u'/n'), (u'：', u'/w'), (u'021', u'/m'), (u'-', u'/nx'), (u'23445612', u'/m'), (u',', u'/w'), (u'蓝翔', u'/nt'), (u'给', u'/p'), (u'宁夏', u'/ns'), (u'固原市', u'/ns'), (u'彭阳县红河镇黑牛沟村3组', u'/nt'), (u'刘能', u'/nr'), (u'捐赠', u'/v'), (u'了', u'/ule'), (u'挖掘机', u'/n'), (u',', u'/w'), (u'地址', u'/n'), (u'：', u'/w'), (u'湖北省', u'/ns'), (u'武汉市洪山区珞瑜路129号', u'/nt'), (u'上海市', u'/ns'), (u'杨浦区', u'/ns'), (u'四平路', u'/nz'), (u'1239号同济大学', u'/nt')]
    
    #建立词典，保存index
    address_dic,facetlist=make_address_dic(textlist)

    #结果字典
    output=process(address_dic,facetlist)
    print output
    
if __name__=='__main__':
    main()