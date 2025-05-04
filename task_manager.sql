-- Task Manager Database Schema
CREATE DATABASE IF NOT EXISTS TaskManagerDB;
USE TaskManagerDB;

CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(50) NOT NULL UNIQUE,
    Email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Tasks (
    TaskID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT NOT NULL,
    Title VARCHAR(100) NOT NULL,
    Description TEXT,
    Status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending',
    DueDate DATE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

INSERT INTO Users (Username, Email) VALUES
('john_doe', 'john@example.com'),
('jane_smith', 'jane@example.com');

INSERT INTO Tasks (UserID, Title, Description, Status, DueDate) VALUES
(1, 'Finish project report', 'Complete the final project report', 'In Progress', '2025-05-10'),
(1, 'Team meeting', 'Discuss project deliverables', 'Pending', '2025-05-06'),
(2, 'Review code', 'Go through the new feature branch', 'Completed', '2025-05-02');
