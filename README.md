# PKU盒武器

据说，曾经的北大门户的人员查询功能是可以通过姓名首字母查询的。但后来，因为不知什么原因，此功能被下架了。但这对于热爱开盒的人们来说是不可接受的！！！于是，我便写了这个小工具，恢复了通过首字母查询人员的功能。

本项目使用的爬虫代码和ui代码（本人不会，虽求助kimi）已全部放在此repo中。但鉴于本人初学爬虫不久，所以使用的方法比较简陋，免去了写iaaa login，直接选择手动登录。



> [!CAUTION]
>
> 由于本项目有一定隐私泄露风险，所以爬虫得到的csv文件并没有放上来。如果你是pku学生，并且也想要的话可私聊联系我。（wechat：dj7152） 



## Instructions

### Prerequisites

- Python 3.x
- FirefoxDriver

### Libraries

- csv
- tkinter
- 如果您想自己爬取数据，则还需要selenium和pypinyin

### Usage

直接运行main.py即可，界面如下图所示。

step1. 按照提示选择csv文件。

![1](https://github.com/qqworld-tutu/PKU-Nuclear-Weapon/blob/main/1.png)

step2. 任意输入至少一个查询条件即可，图例为首字母查询。

![2](https://github.com/qqworld-tutu/PKU-Nuclear-Weapon/blob/main/2.png)

## 免责声明

1. 本仓库严禁用于任何商业用途！
2. 如果您已经有了csv文件，请勿随意传播！
