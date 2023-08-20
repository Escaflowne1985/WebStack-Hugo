
安装和Linux环境配置文字流程： [WebStackHugo导航开源项目部署流程和内容一键配置](https://datayang.blog.csdn.net/article/details/127744116)

本项目是基于纯静态的网址导航网站 [webstack.cc](https://github.com/WebStackPage/WebStackPage.github.io) 制作的Hogo主题，基于开源项目的基础这里总结了一下在 centos7 云服务器部署和本地一键配置数据更新静态页面的笔记。

不得不说 Hugo 比 Django 利用开源的项目基础二次开发和数据整理要方便快捷很多。

先来看一下 [我的主页吧](https://home.datayang.cn/)。由于懒很多icon没有更新，将就能用，个人感觉相比源码来说亮点在于直接更新excel就可以直接导出data目录下webstack.yml文件直接使用。

数据处理格式以及文件脚本在 `data_process` 文件夹下。

获取每个网站的icon爬虫脚本图标在`icon_process` 文件夹下。

nginx配置在`conf`文件夹下的`nginx.conf`文件自行配置即可。

![在这里插入图片描述](https://img-blog.csdnimg.cn/08cf246dc61c4b319ea6c9de9bffd188.png)![在这里插入图片描述](https://img-blog.csdnimg.cn/9f4e4cbdaf424bdd821c30b7f82147ca.png)