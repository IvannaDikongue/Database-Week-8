CREATE DATABASE TaskManagerDB;
USE TaskManagerDB;

CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending',
    due_date DATE,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

INSERT INTO Users (username, email) VALUES
('john_doe', 'john@example.com'),
('jane_smith', 'jane@example.com');

INSERT INTO Tasks (title, description, status, due_date, user_id) VALUES
('Finish report', 'Complete the annual report', 'In Progress', '2025-05-10', 1),
('Team meeting', 'Discuss project updates', 'Pending', '2025-05-06', 1),
('Code review', 'Review the new feature branch', 'Completed', '2025-05-02', 2);
