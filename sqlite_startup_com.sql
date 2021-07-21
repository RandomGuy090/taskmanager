CREATE VIEW main_page_info as
SELECT
taskmanager_user.name as user,
taskmanager_user.profImg as prof_pic,
taskmanager_tables.id as table_id,
taskmanager_tables.name as table_name,
taskmanager_tables.url as table_url,
taskmanager_tables.color as table_color,
taskmanager_tables.borderColor as table_b_color
FROM
taskmanager_particip
LEFT JOIN taskmanager_user ON taskmanager_particip.userId_id = taskmanager_user.id
LEFT JOIN taskmanager_tables ON taskmanager_particip.tableId_id = taskmanager_tables.id
;
CREATE VIEW list_users_table as
SELECT 
taskmanager_particip.joinedDate as date,
taskmanager_user.id as user_id,
taskmanager_user.name as user_name,
taskmanager_user.profImg as user_prof,
taskmanager_taskcolor.color as user_color,
taskmanager_tables.id as table_id,
taskmanager_tables.url as table_url,
taskmanager_tables.name as table_name,
taskmanager_tables.color as table_color
FROM
taskmanager_particip
JOIN taskmanager_user ON taskmanager_particip.userId_id = user_id
JOIN taskmanager_tables ON taskmanager_particip.tableId_id = table_id
JOIN taskmanager_taskcolor ON taskmanager_taskcolor.userId_id = user_id
;
CREATE VIEW get_table_color as
select 
taskmanager_user.name as user_name, 
taskmanager_user.profImg as user_prof, 
taskmanager_taskcolor.color as user_color,
taskmanager_tables.name as table_name ,
taskmanager_tables.url as table_url,
taskmanager_tables.color as table_color
from 
taskmanager_taskcolor 
join taskmanager_tables ON tableId_id = taskmanager_tables.id 
join taskmanager_user  on userId_id = taskmanager_user.id
;
CREATE VIEW get_tasks_info as
select  
taskmanager_tables.name as table_name,
taskmanager_user.name as user,
taskmanager_user.id as user_id,
taskmanager_user.profImg as user_prof_pic,
taskmanager_tables.color as table_color,
taskmanager_taskcolor.color as task_color,
taskmanager_tables.url as table_url,
taskmanager_notes.tableNote as note,
taskmanager_notes.addedDate as added_date,
taskmanager_notes.todoDate_start as to_do_date_start,
taskmanager_notes.todoDate_end as  to_do_date_end,
taskmanager_notes.id as note_id
from 
taskmanager_notes
JOIN taskmanager_user ON taskmanager_notes.userId_id = taskmanager_user.id
JOIN taskmanager_tables ON taskmanager_notes.tableId_id = taskmanager_tables.id
JOIN taskmanager_taskcolor ON taskmanager_notes.userId_id = taskmanager_taskcolor.userId_id AND taskmanager_notes.tableId_id = taskmanager_taskcolor.tableId_id
;
CREATE VIEW get_tasks as
select  
taskmanager_tables.name as table_name,
taskmanager_user.name as user,
taskmanager_user.id as user_id,
taskmanager_user.profImg as user_prof_pic,
taskmanager_tables.color as table_color,
taskmanager_taskcolor.color as task_color,
taskmanager_tables.url as table_url,
taskmanager_notes.tableNote as note,
taskmanager_notes.addedDate as added_date,
taskmanager_notes.todoDate_start as to_do_date_start,
taskmanager_notes.todoDate_end as  to_do_date_end,
taskmanager_notes.id as note_id
from 
taskmanager_notes
JOIN taskmanager_user ON taskmanager_notes.userId_id = taskmanager_user.id
JOIN taskmanager_tables ON taskmanager_notes.tableId_id = taskmanager_tables.id
JOIN taskmanager_taskcolor ON taskmanager_notes.userId_id = taskmanager_taskcolor.userId_id AND taskmanager_notes.tableId_id = taskmanager_taskcolor.tableId_id
;