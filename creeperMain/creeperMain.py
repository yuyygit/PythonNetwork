# encoding: utf-8
import re
import requests


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
}


if __name__ == '__main__':
    for i in range(1,10):
        url = 'https://www.xicidaili.com/nn/{}'.format(i)
        response = requests.get(url,headers = headers)
        print(response.text)
        html = response.text
        ips = re.findall("<td>(\d+\.\d+\.\d+\.\d+)</td>", html, re.S)
        ports = re.findall("<td>(\d+)</td>", html, re.S)
        # print (ips)
        # print(ports)
        ipsAndprots = []
        for ip in zip(ips,ports):
            proxies = {
                "http": "http://" + ip[0] + ":" + ip[1],
                "https": "http://" + ip[0] + ":" + ip[1],
            }
            try:
                res = requests.get("http://www.baidu.com", proxies = proxies,timeout = 3)
                print (ip, u"能使用")
                with open ("ip.text",mode = "a+") as f:
                    f.write(":".join(ip))
            except:
                print (ip, u"不能使用")
    #     ipsAndprots.append(ip)
    # print (ipsAndprots)
    """
    "<td>\d+.204.243.138</td><td>9999</td>",html, re.S
    <td>163.204.243.138</td>
    <td>9999</td>
    """
'''
    获取IP
        市面上免费的IP都会去获取
        
    
    维护IP池
        清洗出可以使用的IP池
        添加IP
        删除
    
    提供服务
'''