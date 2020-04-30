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
select id,name from goods where price > (select round(avg(price),2) as avg_price from goods) order by price desc;
-- 查询每种类型中最贵的电脑信息
select * from (
    select cate_name,max(price) as max_price from goods group by cate_name
)as g_new left join goods as g on g_new.cate_name=g.cate_name and g_new.max_price=g.price order by g_new.cate_name;

-- 视图 可查看不可修改
create view v_goods_info as select g.*,c.name as cate_name,b.name as brands_name from goods as g left join goods_cates as c on g.cate_id=c.id left join goods_brands as b on g.brand_id=b.id;
