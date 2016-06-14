#=-= coding:utf-8 =-=

import re

#地址的表达式pattern
Address_pattern= u'(/ns)+(/nz)?(/nt)?(/m(/q|/n))?'

#主处理函数
def process(textlist):
    Address_location={}
    #初始化index
    index=0
    #把地址拼接起来：
    Address_key=u''
    #把地址index保存list
    Address_index=[]
    for item in textlist:
        #读取字段和词性
        word,facet=item
        index+=1
        
        if re.search(facet,Address_pattern):
            Address_key+=word
            Address_index.append(index)
            print word,facet,index
        elif len(Address_index)!=0:
            #保存结果并清空key和index
            Address_location[Address_key]=[min(Address_index),max(Address_index)]
            Address_key=u''
            Address_index=[]
            print index,'refresh'
        else:
            print index
    return Address_location
    
    
    
def main():
    textlist=[(u'地址', u'/n'), (u'：', u'/w'), (u'上海市', u'/ns'), (u'杨浦区', u'/ns'), (u'四平路', u'/nz'), (u'1239号同济大学', u'/nt'), (u'，', u'/w'), (u'电话', u'/n'), (u'：', u'/w'), (u'021', u'/m'), (u'-', u'/nx'), (u'23445612', u'/m'), (u',', u'/w'), (u'蓝翔', u'/nt'), (u'给', u'/p'), (u'宁夏', u'/ns'), (u'固原市', u'/ns'), (u'彭阳县红河镇黑牛沟村3组', u'/nt'), (u'刘能', u'/nr'), (u'捐赠', u'/v'), (u'了', u'/ule'), (u'挖掘机', u'/n'), (u',', u'/w'), (u'地址', u'/n'), (u'：', u'/w'), (u'湖北省', u'/ns'), (u'武汉市洪山区珞瑜路129号', u'/nt')]
    #结果字典
    output=process(textlist)
    #print output
    
if __name__=='__main__':
    main()