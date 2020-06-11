# share-your-life
Platform is introduce：It's an open social platform

功能介绍：
  1.登录可账号密码登录，可人脸识别登录
  2.发表文章以及评论
  3.拥有个人空间主页
  4.实现在线聊天
  5.观看实时视频
  6.内置小游戏
  后续待定。。
  
新功能拓展：
  1.抓取代理(获取可靠代理,定时任务更新)

表：
分析
用户表于文章表1对多关系
用户表于评论表1对多关系
文章表于评论表1对多关系
文章分类表于文章表1对多关系

基本功能表

用户表: 
  表名：UserInfo
  字段：id, name, phone, email, sex, face, picture,password, create_time, update_time, is_delete
  
文章表：
  表名：Article
  字段：id, title, picture, content, create_time, update_time, is_delete
  外键：user_info, classify
  
评论表:
  表名：Comment
  字段：id, content, create_time, update_time, is_delete
  外键：article, user_info
  
文章分类表：
  表名：Classify
  字段：id, name, create_time, update_time, comment, is_delete
  
  
系统权限相关表

菜单表：
  表名: SysMenu
  字段：id, name, parent_menu, comment, create_time, update_time, is_delete
  
角色表：
  表名：Rule
  字段：id, name, permission, create_time, comment, update_time, is_delete
  
用户角色表：
  表名：RuleUser
  字段：id, user_account, create_time, comment, update_time, is_delete
  外键：rule
  
权限表：
  表名：Permission
  字段：id, name, type, comment, create_time, update_time, is_delete
  外键：sysmenu
  
  
代理表：
  表名：Proxy
  字段：id, ip, port	secret	request_type	area	response_speed	last_check_time, IP	PORT	匿名度	类型	位置	响应速度	最后验证时间




  

  
  

  
  
  
