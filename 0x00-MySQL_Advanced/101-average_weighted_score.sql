-- Task 13: Create procedure to compute average weighted score for all users
DROP PROCEDURE IF EXISTS ComputerAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUsers()
BEGIN
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    DECLARE done INT DEFAULT 0;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN user_cursor;

    read_loop: LOOP
        FETCH user_cursor INTO @user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        CAL ComputeAverageScoreForUser(@user_id);
    END LOOP;

    CLOSE user_cursor;
END;
$$
DELIMITER ;
