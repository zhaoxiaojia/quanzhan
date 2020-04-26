-- 创建新的关联表
create table if not exists goods_cates(
      id int unsigned primary key auto_increment,
      name varchar(40) not null
      );

-- 查询goods表中的商品种类
select cate_name from goods group by cate_name;

-- 将分组结果写入goods_cate 数据表
insert into goods_cates (name) select cate_name from goods group by cate_name;

-- 通过goods_cates数据表来更新goods表
update goods as g inner join goods_cates as c on g.cate_name=c.name set g.cate_name=c.id;

-- 通过alter table语句修改表结构
alter table goods
change cate_name cate_id int unsigned not null,
change brand_name brand_id int unsigned not null;

-- 给brand_id 添加外键约束
alter table goods add foreign key (brand_id) references goods_brands(id);
-- 给cate_id 添加外键约束
alter table goods add foreign key (cate_id) references goods_cates(id);