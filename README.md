# web_test
web页面自动化测试


#### 问题记录

（一） webdriver.Chrom() 打开失败

解决方法： driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

原理：webdriver_manager自动配置了路径

参考链接：
https://cloud.tencent.com/developer/article/2358863

（二）pytest报错 __init__ constructor

原因：pytest has a __init__ constructor 运行的测试类下边不能包含__init__方法

解决方案：去除父类TestCase中的__init__方法

参考链接：https://www.cnblogs.com/renjie1105/p/15476946.html