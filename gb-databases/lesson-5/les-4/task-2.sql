DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `birthday_at` DATETIME COLLATE utf8_unicode_ci,
  `created_at` DATETIME COLLATE utf8_unicode_ci,
  `updated_at` varchar(25) COLLATE utf8_unicode_ci,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO users (name, birthday_at) VALUES
  ('��������', '1988-02-04'),
  ('��������', '1988-02-04'),
  ('����', '1998-03-20'),
  ('����', '2006-07-13');
 

SELECT TIMESTAMPDIFF(DAY, 
   STR_TO_DATE(CONCAT(CONVERT(YEAR(CURDATE()), CHAR),'-01-01'), '%Y-%m-%d'),
   STR_TO_DATE(CONCAT(CONVERT(YEAR(CURDATE()), CHAR), '-', MONTH(birthday_at), '-', DAY(birthday_at)), '%Y-%m-%d')) % 7 as d, 
   COUNT(*)
FROM users
GROUP BY d;