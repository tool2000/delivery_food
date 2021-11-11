-- 고객 관련 테이블
create table user (
    id varchar(10) primary key,
    delivery_address varchar(100)
);

INSERT INTO user VALUES ("elice", "코더랜드로 1길");
INSERT INTO user VALUES ("dodobird", "코더랜드로 2길");
INSERT INTO user VALUES ("hatseller", "코더랜드로 3길");

-- 음식점 관련 테이블
create table store(
    id varchar(30) primary key,
    store_address varchar(100),
    contact_number varchar(20)
);

INSERT INTO store VALUES ("엘리스 분식", "당근 1길", "02-0000-0000");
INSERT INTO store VALUES ("엘리스 마라탕", "당근 2길", "02-1111-1111");
INSERT INTO store VALUES ("엘리스 중국집", "당근 3길", "02-2222-2222");

-- 음식 관련 테이블
create table menu(
    id varchar(30) primary key,
    store_id varchar(30),
    price int,
    fee int
);

INSERT INTO menu VALUES ("떡볶이", "엘리스 분식", 5000, 3000);
INSERT INTO menu VALUES ("마라탕", "엘리스 마라탕", 9000, 2000);
INSERT INTO menu VALUES ("짜장면", "엘리스 중국집", 7000, 1000);

-- 배달 정보 관련 테이블
create table delivery_order(
    id int auto_increment primary key,
    order_dt timestamp default NOW(),
    user_id varchar(10),
    delivery_address varchar(100),
    menu_id varchar(30),
    store_id varchar(30),
    store_contact_number varchar(20),
    total_price int,
    delivery_fee int,
    order_method enum('card', 'cash')
    
);