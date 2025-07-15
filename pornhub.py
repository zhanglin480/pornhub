#-*-编码：utf-8-*-
进口导入操作系统
进口导入re
进口导入请求



classPornhub类()：():
Def__init__(self，url)：def__init__(self，url):
自己。URL=urlurl=url
自己。ROOTPATH=下行路径+"/"ROOTPATH=下行路径+"/"

定义剖析HTML(自我，URL)(_H)：defparse_html(self，url):
RESP=请求。得到(URL，标题=random_header()，timeout=0.1)得到(URL，标头=random_header()，timeout=0.1)
返回resp.textreturnRESP.文本

定义save_mp4(自，项目)：defsave_mp4(自己，项目):
如果项目["quality_720p"]：if项目["quality_720p"]:
URL=项目["quality_720p"]["quality_720p"]
其他：其他：
URL=项目["quality_480p"]["quality_480p"]
file_path=self。ROOTPATH+再(r"[/\\：*？\"<>|]"，"_"，项目["视频标题"])+".MP4"ROOTPATH+re(r"[/\\：*？\"<>|]"，"_"，项目["视频标题"])+".MP4"
self.download_from_url(url，文件路径，random_header())download_from_url(url，文件路径，random_header())

Def download_from_url(自身、URL、文件路径、标头)：Def download_from_url(自身、URL、文件路径、标头)：
print("开始下载："，文件路径)print("开始下载："，文件路径)
open(filepath，'wb')为f：，open(filepath，'wb')为f：
f。写入(请求。get(url，headers，timeout=0。1)。内容)写入(请求。get(url，headers，timeout=0。1)。内容)

Def运行(自身)：Def run(self)：
尝试：尝试：
URL=self.urlurl
HTML_str=self.parse_html(url)parse_html(url)
项目={}{}
item["video_title"]=re。findall('"视频标题"："(.*？)"，'，html_str)[0]["video_title"]=re.findall('"视频标题"："(.*？)"，'，html_str)[0]
item["quality_720p"]=re.findall('"quality_720p"："(.*？)"，'，html_str)["quality_720p"]=re.findall('"quality_720p"："(.*？)"，'，html_str)
如果项目['quality_720p']：
item["quality_720p"]=item["quality_720p"][0]。取代('\\'，")
item["quality_480p"]=re.findall('"quality_480p"："(.*？)"，'，html_str)
如果项目['quality_480p']：
item["quality_480p"]=item["quality_480p"][0]。取代('\\'，")

self.save_mp4(项目)
例外情况除外，如e：
通过


下行路径="D:/ph/other"


Def random_header()：
返回{
'cookie'："ua=237aa6249591b6a7ad6962bc73492c77；platform_cookie_reset=pc；platform=pc；bs=kkfbi66h9zevjeq5bt27j0rvno182xdl；ss=205462885846193616；RNLBSERVERID=ded6699"，
'user-agent'：'Mozilla/5.0(Windows NT10.0；Win64；x64)AppleWebKit/537.36(KHTML，如Gecko)Chrome/79.0.3945.88Safari/537.36'
    }


download_urls=[
"https://cn.pornhub.com/view_video.php?viewkey=ph5ebbe3985a3fd"，
"https://cn.pornhub.com/view_video.php?viewkey=ph5dc135a0b5f78"，
"https://cn.pornhub.com/view_video.php?viewkey=ph5c33a2296e92d"，
"https://cn.pornhubpremium.com/view_video.php?viewkey=ph5d55ac31a7682"，
]

如果__名称__=='__主要的__'：
如果不存在os.path.(下行路径(_p))：
os.makedirs(下行路径)
print("读取存放目录为："，down_path)
尝试：
打印("将要爬取的链接为：")
对于download_urls中的URL：
打印(url)
对于download_urls中的URL：
P=Pornhub(url)
p.run()

例外情况除外，如e：
打印("\n*"*20)
print("程序运行错误："，e)
打印("*"*20，"\n")
最后：
打印("QQ:2416447718")
打印("QQ:2470571458")
打印("TG：@porsms")
