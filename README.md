# SwiftLeanStrategy
ios项目瘦身套路，swift为主、混编oc、cocoaPods管理的iOS项目的可执行文件减Size详细攻略

相关参考文章传送门 |
---|---
[iOS 可执行文件瘦身方法  -- bang](http://blog.cnbang.net/tech/2544/) | 
[iOS App可执行文件的组成  -- bang](http://blog.cnbang.net/tech/2296/) | 
[清理 iOS 项目不用的图片资源 -- 姜家志](http://ios.jobbole.com/85392/) |
[使用 python 找出 iOS 项目中没有使用到的图片资源 -- hi_xgb](http://www.jianshu.com/p/30c688621fa4) |

## 套路：++三步走++

![image](http://blog.cnbang.net/wp-content/uploads/2015/01/安装包大小优化.png)
1. 删压图片
2. 编译优化 （这个部分本文未包涵，但是这是收效最快的方法，立竿见影！请读者自行查阅相关文章）
3. 删代码

---
## 具体实现方法
这里提供了几个python脚本，用于查找项目中没有被使用的图片资源和代码，下面会介绍使用方法、思路原理和需要注意的地方：
- find_all_func_list.py
- find_all_unuseful_swift_func.py
- find_all_unuseful_swift_file.py
- find_all_unuseful_imageset.py
- find_all_unuseful_png.py	
- linkmap.js

1. ###### 大段代码注释
2. ###### 没有被引用的类
3. ###### 没有被调用的方法
4. ###### image.xcassets中没有被使用的图片资源
5. ###### 未被使用的png图片资源
6. ###### 压缩全部图片资源
7. ###### 第三方包的替换和删除

具体请参见简书地址：
[本文简书地址>>](https://www.jianshu.com/p/72b3f48ac045)
