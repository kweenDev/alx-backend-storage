-- Task 10: Create a function SafeDiv to safely divide two numbers
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
DETERMINISTIC
BEGIN
    RETURN IF(b = 0, 0, a / b);
END;
//
DELIMITER ;
