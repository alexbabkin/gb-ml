use vk

SELECT 
(
   (SELECT COUNT(*) FROM likes
       WHERE user_id IN (SELECT user_id FROM profiles WHERE gender = 'f')) -
   (SELECT COUNT(*) FROM likes
       WHERE user_id IN (SELECT user_id FROM profiles WHERE gender = 'm')) 
)