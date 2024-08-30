# web_test
web页面自动化测试

只覆盖最核心且直接影响主营业务流程的 E2E 场景。

#### 框架设计

一、框架总体架构

（一）case

封装用例和输入数据

输入数据形式
1. 实时创建数据：On-the-fly
2. 事先创建测试数据：Out-of-box

（二）step

封装步骤

（三）page

封装页面，使用page object模式

(1) 操作函数的粒度

按照业务流程进行细化，登录、注册、查询作为一个函数使用

(2) 衔接两个操作函数之间的页面

按照业务流程，获得当前业务的执行页面，也就是初始页面

执行页面
1. 默认创建的页面
2. 上一个业务函数执行后的业务

#### 待实现

（一）Headless Chrome

（二）截图记录

利用 Selenium WebDriver 的 screenshot 函数在一些特定的时机（比如，页面发生跳转时，在页面上操作某个控件时，或者是测试失败时，等等）完成界面截图功能。

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
