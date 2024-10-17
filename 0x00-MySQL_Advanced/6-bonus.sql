-- Task 6: Create procedure to add a bonus for a student
DELIMITER |
CREATE PROCEDURE AddBonus(
    IN user_id int,
    IN project_name varchar(255),
    IN score float
    )
    BEGIN
        INSERT INTO projects (name)
        SELECT project_name FROM DUAL

        --- Check if project exists, if not, create it
        WHERE NOT EXISTS (SELECT * FROM projects WHERE name = project_name);
        -- Add correction for the user
        INSERT INTO corrections (user_id, project_id, score)
        VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END;
|