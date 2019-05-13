#Task 1
##1.1 MySQL软件安装及数据库基础
- 软件安装及服务器设置：
    1. 首先先到MySQL的官网下载压缩文件。
    2. 解压到C:\web\mysql-8.0.11
    ```
    [mysql]
    # 设置mysql客户端默认字符集
    default-character-set=utf8
    
    [mysqld]
    # 设置3306端口
    port = 3306
    # 设置mysql的安装目录
    basedir=C:\\web\\mysql-8.0.11
    # 设置 mysql数据库的数据的存放目录，MySQL 8+ 不需要以下配置，系统自己生成即可，否则有可能报错
    # datadir=C:\\web\\sqldata
    # 允许最大连接数
    max_connections=20
    # 服务端使用的字符集默认为8比特编码的latin1字符集
    character-set-server=utf8
    # 创建新表时将使用的默认存储引擎
    default-storage-engine=INNODB
    ```
    3. 以管理员身份打开cmd
    4. 切换到解压的目录：
    ```
    cd C:\web\mysql-8.0.11\bin
    ```
    5. 初始化数据库：
    ```
    mysqld --initialize --console
    ```
    执行完之后，会输出root用户的初始默认代码。
    6. 启动MySQL:
    ```
    net start mysql
    ```
    7. 连接MySQL服务器:
    ```
    mysql -uroot -p
    ```
    然后输入密码即可完成服务器的连接
    8. 断开MySQL服务器:
    ```
    exit/quit
    ```
    9. 停止MySQL服务器:
    ```
    net stop mysql
    ```
- 数据库基础知识
    1. 数据库的定义：数据库，是长期存储在计算机内、有组织的、可共享的大量数据的集合。
    2. 关系模式：从用户观点看，关系模式就是由一组关系组成，每个关系的数据结构是一张规范的二维表。
    3. 二维表：至少有部分列是非独立的，同类概念/属性/参数（可归类为一类），那么就是二维表，主要目的是展示，更容易理解，发现规律。
    - 一维表：每列都是独立属性，列和列之间不能在归为1类概念，录入原始数据，一般要有一维表
    比如：
    ```
    表1： 姓名，数学，语文，物理，化学---二维表

    表2：姓名，学科，成绩---一维表
    ```
    4. 行代表了每个特性定的对象。
    5. 列是特定对象的属性。
    6. 主键：能够唯一地标识一个元组的属性或属性组称为关系的键或候选键。 若一个关系有多个候选键则可选其一作为主键(Primary key)。
    7. 外键：如果一个关系的一个或一组属性引用(参照)了另一个关系的主键，则称这个或这组属性为外码或外键(Foreign key)。
- MySQL数据库管理系统
    1. MySQL数据库管理系统：是专门用于管理数据库的计算机系统软件。数据库管理系统能够为数据库提供数据的定义、建立、维护、查询和统计等操作功能。并完成对数据完整性、安全性进行控制的功能
    2. 数据库：数据库，是长期存储在计算机内、有组织的、可共享的大量数据的集合。
    ···
    #创建数据库
    CREATE DATABASE 数据库名；
    ····
    ```
    #删除数据库
    drop database <数据库名>;
    ```
    ```
    #选择数据库
    [root@host]# mysql -u root -p
    Enter password:******
    mysql> use 数据库名;
    ```
    3. 表：真正的存在与数据库中（也就是硬件介质上）的数据组合。
    ```
    CREATE TABLE table_name(column_name column_type)ENGINE=InnoDB DEFAULT CHARSET=utf8;
    - PRIMARY KEY关键字用于定义列为主键。 您可以使用多列来定义主键，列间以逗号分隔。
    - ENGINE 设置存储引擎，CHARSET 设置编码。
    ```
    ```
    #删除数据表
    DROP TABLE table_name;
    ```
    4. 视图：是一张虚拟的表，其内容由查询定义；简单的说视图就是由select结果集组成的表。每次访问视图的时候，系统会自动根据视图的规则去组织筛选数据。
    5. 存储过程：是一种在数据库中存储复杂程序，以便外部程序调用的一种数据库对象。
##MySQL基础（一）- 查询语句
1. 导入数据库
    连接到MySQL服务器并创建数据库
    ```
    #连接数据库
    mysql -uroot -p
    #创建数据库
    CREATE DATABASE IF NOT EXISTS CHARSET utf8 COLLATE utf8_general_ci;
    use yiibaidb;
    #导入数据
    use yiibaidb;
    source D:/data/yiibaidb.sql;
    #测试导入结果
    select city,phone,country from `offices`;
    ```
    出现ERROR 1820 (HY000): You must reset your password using ALTER USER statement before executing this statement.
    解决方法：
    - ALTER USER USER() IDENTIFIED BY 'q18978718259';
    - ALTER USER 'root'@'localhost' PASSWORD EXPIRE NEVER;
    - FLUSH PRIVILEGES;
    - quit后，重新使用新密码登陆即可进行操作了。
2. **sql是什么？**
- SQL是Structured Query Language(结构化查询语言)的缩写。SQL是专为数据库而建立的操作命令集，是一种功能齐全的数据库语言。在使用它时，只需要发出“做什么”的命令，“怎么做”是不用使用者考虑的。
**MySQL是什么？**
- 是一个关系型数据库管理系统，由瑞典MySQL AB 公司开发，目前属于 Oracle 旗下产品。MySQL 是最流行的关系型数据库管理系统之一，在 WEB 应用方面，MySQL是最好的 RDBMS (Relational Database Management System，关系数据库管理系统) 应用软件。
3. 查询语句 SELECT FROM
```
SELECT column_name,column_name
FROM table_name
[WHERE Clause]
[LIMIT N][ OFFSET M]
```
- 查询语句中你可以使用一个或者多个表，表之间使用逗号(,)分割，并使用WHERE语句来设定查询条件。
- SELECT 命令可以读取一条或者多条记录。
- 你可以使用星号（*）来代替其他字段，SELECT语句会返回表的所有字段数据
- 你可以使用 WHERE 语句来包含任何条件。
- 你可以使用 LIMIT 属性来设定返回的记录数
- 你可以通过OFFSET指定SELECT语句开始查询的数据偏移量。默认情况下偏移量为0。

**去重语句：**
    - SELECT 语句中使用 DISTINCT 关键字来过滤重复数据。
    ```
    SELECT DISTINCT last_name, first_name FROM person_tbl;
    ```
    - 使用 GROUP BY 来读取数据表中不重复的数据:
    ```
    SELECT last_name, first_name FROM person_tbl GROUP BY (last_name, first_name)
    ```
**前N个语句**
使用SELECT的关键字LIMIT来返回记录数
```
#去第0到第30的数据
SELECT * FROM TABLE LIMIT 0, 10
```
**CASE...END判断语句**
```
SELECT            
    CESE                   -------------如果
    WHEN sex='1' THEN '男' -------------sex='1'，则返回值'男'
    WHEN sex='2' THEN '女' -------------sex='2'，则返回值'女'
    ELSE 0                 -------------其他的返回'其他’
    END                    -------------结束
from   sys_user            --------整体理解： 在sys_user表中如果sex='1'，则返回值'男'如果sex='2'，则返回值'女' 否则返回'其他’
```
4. 筛选语句 WHERE 
有条件地从表中选取数据，可将 WHERE 子句添加到 SELECT 语句中。
```
SELECT field1, field2,...fieldN FROM table_name1, table_name2...
[WHERE condition1 [AND [OR]] condition2.....
```
- 查询语句中你可以使用一个或者多个表，表之间使用逗号, 分割，并使用WHERE语句来设定查询条件。
- 你可以在 WHERE 子句中指定任何条件。
- 你可以使用 AND 或者 OR 指定一个或多个条件。
- WHERE 子句也可以运用于 SQL 的 DELETE 或者 UPDATE 命令
- WHERE 子句类似于程序语言中的 if 条件，根据 MySQL 表中的字段值来读取指定的数据。

**通配符:**
=	，检测两个值是否相等，如果相等返回true,(A = B)返回false。
<>, !=，检测两个值是否相等，如果不相等返回true,(A != B)返回 true。
\>，检测左边的值是否大于右边的值, 如果左边的值大于右边的值返回true,(A > B)返回false。
<，检测左边的值是否小于右边的值, 如果左边的值小于右边的值返回true,(A < B)返回true。
\>=，检测左边的值是否大于或等于右边的值, 如果左边的值大于或等于右边的值返回true,(A >= B)返回false。
<=，检测左边的值是否小于于或等于右边的值, 如果左边的值小于或等于右边的值返回true,(A <= B)返回true。
5. 分组语句GROUP BY
GROUP BY 语句根据一个或多个列对结果集进行分组。在分组的列上我们可以使用 COUNT, SUM, AVG,等函数。
```
SELECT column_name, function(column_name)
FROM table_name
WHERE column_name operator value
GROUP BY column_name;
```

- 聚集函数
聚集函数是以值是一个集合（集或者多重集）为输入、返回单个值得函数。SQL提供了五个固有聚集函数。
平均值：avg
最小值：min
最大值：max
总和：sum
计数：count
```
-- 找出教师的平均工资
SELECT AVG (salary)
FROM instructor
--找出名字的个数，这里的distinct作用是是的重复的元素不被计数
SELECT COUNT(DISTINCT name)
FROM instructor;
```
- 分组聚集
如果希望将聚集函数作用在单个元组集上，也希望作用到一组元组集上，此时可以利用group by子句来实现。
group by 子句作用：对给出的一个或多个属性来构造分组，将属性上取值相同的元组分到同一组中。
```
# 找出每个系的教师平均工资
SELECT dept_name, avg(salary) AS avg_salary
FROM instructor
GROUP BY dept_name;
```
**注意：** 当SQL查询使用分组的时候，需要保证出现在select语句中但没有被聚集的属性只能是出现在group by 子句中的那些属性。换句话说，任何没有出现在group by子句中的属性如果出现在select子句中的话，它只能出现在聚集函数的内部，否则这样的查询就是错误的，例如：
```
SELECT dept_name,id,avg(salary) as avg_salary
FROM instructor
GROUP BY dept_name;
```

- having子句
是限定分组条件的语句，针对的是GROUP BY子句构成的分组，即having子句是在分组之后才生效的。
```
SELECT dept_name,avg(salary) as avg_salary
FROM instructor
GROUP BY dept_name
HAVING avg(salary)>15000;
```
**注意：** 与select子句的情况类似，任何出现在having子句中，但没有被聚集的属性必须出现在group by子句中，否则查询就被当成是错误的。
6. 排序语句 ORDER BY
如果我们需要对读取的数据进行排序，我们就可以使用 MySQL 的 ORDER BY 子句来设定你想按哪个字段哪种方式来进行排序，再返回搜索结果。
```
SELECT field1, field2,...fieldN table_name1, table_name2...
ORDER BY field1, [field2...] [ASC [DESC]]
```
- 你可以使用任何字段来作为排序的条件，从而返回排序后的查询结果。
- 你可以设定多个字段来排序。
- 你可以使用 ASC 或 DESC 关键字来设置查询结果是按升序或降序排列。 默认情况下，它是按升序排列。
- 你可以添加 WHERE...LIKE 子句来设置条件。
7. 函数
[可以在点击这里查](https://www.runoob.com/mysql/mysql-functions.html)
8. MySQL注释
\#DELETE FROM SeatInformation 
/*DELETE FROM SeatInformation */
-- DELETE FROM SeatInformation(注意空格)
#因为前几天在准备面试，还没有写代码，和看代码规范