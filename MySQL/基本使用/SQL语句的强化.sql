-- 查询类型cate_name 为’超极本'的商品名称，价格
select name,price from goods where cate_name = '超级本';
-- 显示商品的种类
select cate_name from goods group by cate_name;
-- 求所有电脑产品的平均价格，并且保留两位小数
select round(avg(price),2) from goods;
-- 显示每种商品的平均价格
select cate_name,avg(price) from goods group by cate_name;
-- 查询每种类型中商品中 最贵，最便宜，平均价，数量
select cate_name,max(price),min(price),avg(price),count(*) from goods group by cate_name;
-- 查询所有价格大于平均价格的商品，并且按照价格降序排序
select * from goods where price > (select avg(price) from goods);
-- 查询每种类型中最贵的电脑信息