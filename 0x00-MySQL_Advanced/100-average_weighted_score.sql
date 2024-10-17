-- Task 12: Create procedure to compute average weighted score for a user
DROP PROCEDURE IF EXISTS ComputerAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE weighted_avg_score FLOAT;

    -- Calculate the weighted average score
    SELECT SUM(score * weight) / SUM(weight) INTO weighted_avg_score
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE user_id = user_id;

    -- Update user's average score
    UPDATE users SET average_score = weighted_avg_score WHERE id = user_id;
END;
$$
DELIMITER ;
