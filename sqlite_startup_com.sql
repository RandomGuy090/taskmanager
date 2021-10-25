CREATE VIEW main_page_info as
SELECT
taskmanager_user.name as user,
taskmanager_user.prof_img as prof_pic,
taskmanager_tables.id as table_id,
taskmanager_tables.name as table_name,
taskmanager_tables.url as table_url,
taskmanager_tables.color as table_color,
taskmanager_tables.border_color as table_b_color
FROM
taskmanager_particip
LEFT JOIN taskmanager_user ON taskmanager_particip.user_id_id = taskmanager_user.id
LEFT JOIN taskmanager_tables ON taskmanager_particip.table_id_id = taskmanager_tables.id
;
CREATE VIEW list_users_table as
SELECT 
taskmanager_particip.joined_date as date,
taskmanager_user.id as user_id,
taskmanager_user.name as user_name,
taskmanager_user.prof_img as user_prof,
taskmanager_task_color.color as user_color,
taskmanager_tables.id as table_id,
taskmanager_tables.url as table_url,
taskmanager_tables.name as table_name,
taskmanager_tables.color as table_color
FROM
taskmanager_particip
JOIN taskmanager_user ON taskmanager_particip.user_id_id = user_id
JOIN taskmanager_tables ON taskmanager_particip.table_id_id = table_id
JOIN taskmanager_task_color ON taskmanager_task_color.user_id_id = user_id
;
CREATE VIEW get_table_color as
select 
taskmanager_user.name as user_name, 
taskmanager_user.prof_img as user_prof, 
taskmanager_task_color.color as user_color,
taskmanager_tables.name as table_name ,
taskmanager_tables.url as table_url,
taskmanager_tables.color as table_color
from 
taskmanager_task_color 
join taskmanager_tables ON table_id_id = taskmanager_tables.id 
join taskmanager_user  on user_id_id = taskmanager_user.id
;
CREATE VIEW get_tasks_info as
select  
taskmanager_tables.name as table_name,
taskmanager_user.name as user,
taskmanager_user.id as user_id,
taskmanager_user.prof_img as user_prof_pic,
taskmanager_tables.color as table_color,
taskmanager_task_color.color as task_color,
taskmanager_tables.url as table_url,
taskmanager_notes.table_note as note,
taskmanager_notes.added_date as added_date,
taskmanager_notes.todo_date_start as to_do_date_start,
taskmanager_notes.todo_date_end as  to_do_date_end,
taskmanager_notes.id as note_id
from 
taskmanager_notes
JOIN taskmanager_user ON taskmanager_notes.user_id_id = taskmanager_user.id
JOIN taskmanager_tables ON taskmanager_notes.table_id_id = taskmanager_tables.id
JOIN taskmanager_task_color ON taskmanager_notes.user_id_id = taskmanager_task_color.user_id_id AND taskmanager_notes.table_id_id = taskmanager_task_color.table_id_id
;
CREATE VIEW get_tasks as
select  
taskmanager_tables.name as table_name,
taskmanager_user.name as user,
taskmanager_user.id as user_id,
taskmanager_user.prof_img as user_prof_pic,
taskmanager_tables.color as table_color,
taskmanager_task_color.color as task_color,
taskmanager_tables.url as table_url,
taskmanager_notes.table_note as note,
taskmanager_notes.added_date as added_date,
taskmanager_notes.todo_date_start as to_do_date_start,
taskmanager_notes.todo_date_end as  to_do_date_end,
taskmanager_notes.id as note_id
from 
taskmanager_notes
JOIN taskmanager_user ON taskmanager_notes.user_id_id = taskmanager_user.id
JOIN taskmanager_tables ON taskmanager_notes.table_id_id = taskmanager_tables.id
JOIN taskmanager_task_color ON taskmanager_notes.user_id_id = taskmanager_task_color.user_id_id AND taskmanager_notes.table_id_id = taskmanager_task_color.table_id_id
;