# proxyAddressCopy
自动复制代理地址 用于Qiu Proxy\
历史发布请加入：https://kook.vip/vf8WWl\
原理是使用QQ mail官方api 并筛选符合Qiu Proxy格式的邮件\
实现较为简单 注释很详细 希望你能看懂
# 教程
1. 打开wx.mail.qq.com登录你Qiu绑定的QQ
2. 点击右上角设置 下滑找到第三方服务 开启并复制授权码
3. 首次启动程序 会生成一个config.json在程序目录下 关闭程序并打开它
4. 将QQmail_account替换为你的QQ邮箱 格式：QQ号@qq.com
    - 将QQmail_authorization_code替换为你复制的授权码
    - 将proxy_route_serial_number (number!!)替换为要使用的线路（数字 从上往下 以实际邮件为准）保存
5. 启动程序
6. 安慕希————启动！
7. /start
8. 程序会自动复制地址你粘贴即可
# 已完成
- [x] 主体逻辑
- [x] 日志、欢迎、Banner及报错
- [x] 配置系统
# 待做
- [ ] GUI
- [ ] 最小化到托盘 及提醒
- [ ] 优化逻辑提高健壮性减小体积
- [ ] c++重构（？
