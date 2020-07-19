# books
小说网站：vue+mysql+flask+scrapy
# git 使用方法
git clone url 把github仓库放到本地
git status 查看提交文件状态
git add. 打包所有的文件
git commit -m '这里就是所需的注释'
git pull 拉代码
git push 提交代码

# 开发环境选择 Ubuntu16.04 linux系统
开发效率高 执行速度快
# 在linux中安装mysql
依次输入三条命令 
apt-get install mysql-server
apt-get install mysql-client
 sudo apt install libmysqlclient-dev
 
 验证安装成功
 netstat -tap | grep mysql
(一般安装好mysql就自动启动进入mysql命令行即可远程登录)
 
 开启远程控制（windows上连接linux系统的mysql数据库）
 现在设置mysql允许远程访问，首先编辑文件/etc/mysql/mysql.conf.d/mysqld.cnf：编辑配置文件就输入命令 
 sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
 
 1.注释掉bind-address = 127.0.0.1：
 2.mysql -u -p‘密码’ 进入mysql命令行
 3.GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '你的密码' WITH GRANT OPTION;
 4.刷新配置 flush privileges;  
 5.exit;退出msql并重启service mysql restart
 6.ip addr 查看本机ip地址
 7.输入ip 端口默认3306 密码 即可远程连接mysql
 
 # mysql操作命令(可查看mysql教程)
 取消外键约束 set foreign_key_checks=0;
 添加外键约束 set foreign_key_checks=1;
 删除表中数据 truncate table+表名；
 添加表中数据 insert into (表的键) values(内容)
 特别注意： 在mysql中，引号会导致一直报错，注意引号为英文
 order by 是用于排序使用，而group by是配合聚合函数count（）来分组
 arg() 求平均值 having过滤(>=90选出大于等于90以上的)要配合group by来使用
 from  表1 inner join 表2 on 表1.column_name=表2.column_name;内连接显示相同的，类似数学中2个集合的交集
 limit 限制查询，用于分页查询 limit s,n s为索引 n为返回数量
 temp 临时表