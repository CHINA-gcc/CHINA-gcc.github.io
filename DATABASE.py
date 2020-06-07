from common_utils import UtilsFunction


class DbApi(UtilsFunction):
    """###"""
    def datail_contents(self):
        # if self.str_input in ["redis_API", "Redis_API", "REDIS_API", "API", "api", "Api"]:
        if self.str_input == "Redis_Api":
            self.detail_infos = """>>> 连接 Redis

    redis.Redis()  
    redis.StricRedis(                   为了兼容旧版本(推荐使用).
        host='localhost',               默认值不填，一般不会外网远程连接redis.
        port=6379,                      默认端口.
        db=0,  # 默认数据库
        decode_response=True            设置为True返回的数据格式就是str类型.
                                        默认为False返回的数据格式是bytes类型.
"""
            print(self.detail_infos)
        elif self.str_input == "MySQL_Api":
            self.detail_infos = """>>> Simple usage
- Create a new connection.

    import pymysql
    conn = pymysql.connect(
        user="...",
        password="...",
        db="...",
        charset="utf8" 
    )
- Create a user(Similar to a car that transmits data).

    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
---This parameter can be returned as a dictionary.

- Execute SQL statement

　　sql = "..."
　　cursor.execute(sql)

- Proactively get results.

    res1 = cursor.fetchone()
    res2 = cursor.fetchone()　　　　　　　　　　　　　　　　　　　　　　
    res3 = cursor.fetchmany(3)　　　　　　　　　　　　　　　　　　　　　　
    res4 = cursor.fetchall()

    cursor.close()
    conn.close()

>>> Advanced usage

    import pymysql
    db_config = {
        "user": "root",
        "password": "qwe123",
        "db": "TanZhou",
        "charset": "utf8"
    }
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        sql = "..."
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
            """
            print(self.detail_infos)
        elif self.str_input == "MySQL_Basic":
            self.detail_infos = """13213
231213
321321
321321
321321
321321
321321
3213213
3213213
3213
3213

            >>>  Library level command
show database;          Display all libraries.
create database db_name charset=utf8; / create database if not exists db_name;         Create the database.
drop database db_name; / drop database if exists db_name;        Delete the database.
use db_name;                   Enter the database.
>>> Table level command
show tables;
desc <table>;                 Specific contents of display table.
create table table_name(id int, parameter varchar(128), parameter enum("parameter1"，"parameter2"));     
show create table table_name; 　　　　　　　　　　　Display creation information.
drop table table_name; / drop table if exists table_name; 　　　Delete table.
>>> CRUD --Insert data
insert into table_name (...) values (...);                Insert the specified field.
insert into table_name values (...);                       Full field insertion.
insert into table_name values (...),(...);                Multi line insertion.
>>> CRUD --Query data
select * from table_name;          　　Full field query.
select ... from table_name;  　　　　　Specified field query.
select * from table_name where ...=...; / select * from table_name where ...>...;   　　　Conditional query.
>>> CRUD --Delete data
>>> CRUD --Update data
update table_name set ...=...;  　　　　       Modify all data in a field.
update table_name set ...=... where ...=...;     Modify all data in multiple fields.
update table_name set ...=... where ...=...;      Modify eligible data.
Be sure to add where.
>>> Screening conditions --Comparison operator
=                           Be equal to.
!=　　　　　　　　　　　　　　　　Not equal to.
is null　　　　　　　　　　　　　Empty.
is not null                  Not empty.
>>> Screening conditions --Logical operator(and / or / not)
>>> Screening conditions --Other operations
order by ... asc　　　　　　　　　　　　　       Ranking from small to large.
order by ... desc　　　　　　　　　　　　　     Ranking from large to small.
order by ... limit n　　　　　　　　　　　　　 So long as n.　
order by ... limit n, m　　　　　　　　　　　　Offset n, get m from n+1.　　　　　
select distinct field from table_name　　　　　 Remove duplication.
>>> Screening conditions --Fuzzy query
select * from table_name where field like "%...%";　　　  % 代表任意多个字符, like 与 where 连用.

select * from table_name where field like "__";　　　　　查询两个字符, _ 代表任意一个字符, 

如果 like 不和 % 或 _ 就和 = 一样的效果.
>>> Screening conditions --Scope query
elect * from table_name where field between ... and ...;
between a and b　　　　　　　　　　　　　　　　　　                 Continuous range, including a , b.
select * from table_name where field in ("...", "...");
in　　　　　　　　　　　　　　　　　　　　　　　　                   Interval range.
>>> Aggregation and grouping --Statistics
select count(...) from table where ...>...;    　　　　　　　　　　　　　　　　Generally write id.
select sum(...) from table where ...;       　　　　　　　　　　　　　　　　　　Summation.
select avg(...) from table;     　　　　　　　　　　　　　　　　　　　　　　　　　　Average value.
select max(...) from table;  　　　　　　　　　　　　　　　　　　　　　　　　　　　 Maximum value.
All tables are replaced by tables！
>>> Aggregation and grouping --Groping
elect field1, field2 from table_name group by field;
select field1, field2 as field3 from table_name group by field;　　　　　　　　 as 代表别名.
having                                                              Where keywords cannot be used with statistical 
    functions. 
select field1, field2 as field3 from table_name group by field having ...
select field1, field2 as field3 from table_name where field like "%...%" group by field having ...
A query statement contains alias(as) 、aggregation functions、where and having，It first executes where,then aggregation 
    functions and alias,and finally having. Where condition should be written before group by.
>>> Subquery
select * from table_name where field1 < (select avg(field2) from table_name);
select * from table_name1.field1, table_name.field2 from (select * from table_name0 where ...) as table_name1;
>>> Join query --Inner join
select * from table_name1 inner join table_name2;　　　　　　　　　　　　　　　　　　无条件内连接 / 交叉连接 / 笛卡尔连接.
select table_name.field from table_name1 inner join table_name2 on field1=field2;　　　　有条件内连接. 
>>> Join query --External connection
left join　When two tables are joined, if the join conditions do not match, the data in the left table is retained, 
    while the right table is filled with NULL.
right join　When two tables are joined, if the join conditions do not match, the data in the right table is retained, 
    while the left tables is filled with NULL.
            """
            print(self.detail_infos)
        else:
            pass
            

dbapi = DbApi([{"MySQL": "MySQL_Basic/MySQL_Api", "Redis": "Redis_Basic/Redis_Api", "MongoDB": "MongoDB_Basic/MongoDB_Api"}])
dbapi.judge_options()
