## PO模式简介

> PO模型是:Page Object Model的简写 页面对象模型
>
> PO设计模式是Selenium自动化测试中最佳的设计模式之一，主要体现在对界面交互细节的封装

**作用：**

​	就是把测试页面和测试脚本进行分离，即把页面封装成类，供测试脚本进行调用;
​	分层机制，让不同层去做不同类型的事情，让代码结构清晰，增加复用性。

**结构分层：**

- **base**			封装每个页面中相同的属性和方法，比如：元素定位、输入、点击等；
- **page object** 		每个页面定义一个类，类中主要包含业务的操作逻辑，将其封装成具体的方法；
- **test case** 			 使用测试数据，组装page object的操作逻辑，生成具体的测试用例

**优点：**

1. 提高代码的可读性
2. 减少了代码的重复
3. 提高代码的可维护性，特别是针对UI界面频繁的项目

**缺点：**

1. 造成项目结构比较复杂，因为是根据流程进行了模块化处理

