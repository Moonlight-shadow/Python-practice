/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50621
Source Host           : J701-51-PC:3306
Source Database       : nodes

Target Server Type    : MYSQL
Target Server Version : 50621
File Encoding         : 65001

Date: 2015-12-03 20:11:46
*/
create Database if not EXISTS `nodes`;
use `nodes`;

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for capacity
-- ----------------------------
DROP TABLE IF EXISTS `capacity`;
CREATE TABLE `capacity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(20) NOT NULL,
  `avai` bigint(20) NOT NULL,
  `used` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ip` (`ip`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for files
-- ----------------------------
DROP TABLE IF EXISTS `files`;
CREATE TABLE `files` (
  `hostid` int(11) NOT NULL,
  `filename` varchar(255) NOT NULL,
  `size` bigint(11) unsigned zerofill DEFAULT NULL,
  PRIMARY KEY (`hostid`,`filename`),
  UNIQUE KEY `filename` (`filename`),
  CONSTRAINT `files_ibfk_1` FOREIGN KEY (`hostid`) REFERENCES `capacity` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
