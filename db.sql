CREATE DATABASE IF NOT EXISTS `todolist`;

use `todolist`;

CREATE TABLE `user` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `username` varchar(20) NOT NULL,
    `password` varchar(255) NOT NULL DEFAULT '',
    `nick_name` varchar(25) NOT NULL DEFAULT '',

    PRIMARY KEY (`id`),
    KEY `idx_username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `list` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `title` VARCHAR(50) NOT NULL,
    `content` TEXT NOT NULL,
    `status` TINYINT(2) NOT NULL DEFAULT 0 COMMENT '完成状态，0/未完成，1/已完成，2/已过期',
    `time` DATETIME NOT NULL,
    `delete_at` TIMESTAMP NULL,
    `user_id` INT NOT NULL,

    PRIMARY KEY (`id`),
    KEY `idx_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

-- INSERT INTO `user`(`username`, `password`, `nick_name`) VALUES('admin', '', 'admin');

-- INSERT INTO `list`(`title`, `content`, `status`, `time`, `user_id`) VALUES('test', 'test', 0, 2020-6-1 8:20:20, 1);
