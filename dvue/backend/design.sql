-- 藏红花
CREATE DATABASE saffron;
USE saffron;

-- 用户数据表
CREATE TABLE user
(
  id INT UNSIGNED AUTO_INCREMENT,       -- 用户ID
  email VARCHAR(254) NOT NULL,          -- 电子邮件
  pwd CHAR(44) NOT NULL,                -- 用户密码
  nickname NVARCHAR(26) DEFAULT NULL,   -- 用户昵称
  is_staff TINYINT(1) DEFAULT 0,        -- 是否为管理人员
  is_active TINYINT(1) DEFAULT 0,       -- 账号是否可用
  last_login DATETIME DEFAULT NULL,     -- 最后登录的时间
  date_joined DATETIME NOT NULL,        -- 加入网站的时间
  PRIMARY KEY (`id`)
)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4

-- 弹幕数据表
CREATE TABLE danmaku
(
  _id INT UNSIGNED AUTO_INCREMENT,    -- 弹幕ID
  id BIGINT UNSIGNED NOT NULL,        -- 弹幕影片ID
  author INT UNSIGNED NOT NULL,       -- 弹幕发送者
  content TEXT NOT NULL,              -- 弹幕内容
  color INT NOT NULL,                 -- 弹幕颜色
  _time DOUBLE NOT NULL,              -- 弹幕出现的时间
  _date DATETIME NOT NULL,            -- 弹幕发送的时间
  ip CHAR(15) NOT NULL,               -- 弹幕发送者IP
  PRIMARY KEY (`_id`)
)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4
