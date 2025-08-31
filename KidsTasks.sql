CREATE DATABASE KidTasks;
USE KidTasks;

CREATE TABLE Tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    child_name VARCHAR(50) NOT NULL,
    task_description VARCHAR(100) NOT NULL,
    is_completed BOOLEAN DEFAULT FALSE,
    stars_earned INT DEFAULT 0
);

INSERT INTO Tasks (child_name, task_description, is_completed, stars_earned)
VALUES 
('Ivan', 'Do homework', TRUE, 1),
('Noah', 'Tidy up', FALSE, 0),
('Sophie', 'Brush your teeth', TRUE, 1),
('Leo', 'Read for 15 minutes', FALSE, 0),
('Zoya', 'Make the bed', TRUE, 1);

SELECT * FROM Tasks;
