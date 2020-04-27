-- 创建新的关联表
create table if not exists goods_cates(
      id int unsigned primary key auto_increment,
      name varchar(40) not null
      );
create table if not exists goods_brands(
      id int unsigned primary key auto_increment,
      name varchar(40) not null
      );
-- 在创建数据表的时候一起插入数据
creta table if not exists goods_brands(
    id int unsigned primary key auto_increment,
    name varchar(40) not null
)select brand_name as name from goods group by brand_name;

-- 查询goods表中的商品种类
select cate_name from goods group by cate_name;

-- 将分组结果写入goods_cate 数据表
insert into goods_cates (name) select cate_name from goods group by cate_name;
insert into goods_brands (name) select brand_name from goods group by brand_name;

-- 通过goods_cates数据表来更新goods表
update goods as g inner join goods_cates as c on g.cate_name=c.name set g.cate_name=c.id;
update goods as g inner join goods_brands as c on g.brand_name=c.name set g.brand_name=c.id;

-- 通过alter table语句修改表结构
alter table goods
change cate_name cate_id int unsigned not null,
change brand_name brand_id int unsigned not null;

-- 给brand_id 添加外键约束
alter table goods add foreign key (brand_id) references goods_brands(id);
-- 给cate_id 添加外键约束
alter table goods add foreign key (cate_id) references goods_cates(id);

-- 取消外键约束
show create table goods;
--  CONSTRAINT `goods_ibfk_1` FOREIGN KEY (`brand_id`) REFERENCES `goods_brands` (`id`),
--  CONSTRAINT `goods_ibfk_2` FOREIGN KEY (`cate_id`) REFERENCES `goods_cates` (`id`)
-- 获取名称之后可以根据名称来删除外键约束
-- alter table goods drop foreign key 外键名称
-- 实际开发中，很少使用外键约束，会极大降低表更新的效率