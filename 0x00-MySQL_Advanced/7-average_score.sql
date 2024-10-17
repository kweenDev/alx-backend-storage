-- Task 7: Create procedure to compute and store the average score for a user
DROP PROCEDURE IF EXISTS ComputerAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;

    -- Calculate the average score
    SET avg_score = (SELECT AVG(score) FROM corrections AS C WHERE C.user_id=user_id);

    -- Update the user's average score
    UPDATE users SET average_score = avg_score WHERE id=user_id;
END
$$
DELIMITER ;
