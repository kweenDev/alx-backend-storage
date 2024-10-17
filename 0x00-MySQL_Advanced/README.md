# 0x00. MySQL Advanced

<img src="https://www.mysql.com/common/logos/logo-mysql-170x115.png" width="100%" height="50%"/>

This project focuses on advanced concepts in MySQL database management. It is designed to enhance your understanding of SQL and prepare you for real-world database challenges. By the end of this project, you will have a solid foundation in implementing and managing complex SQL queries, optimizing database performance, and automating processes with stored procedures and triggers.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Learning Objectives](#learning-objectives)
- [Key Concepts](#key-concepts)
- [Tasks](#tasks)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Author](#author)

---

## Project Overview

The **0x00-MySQL_Advanced** project encompasses a variety of advanced SQL topics that will help you develop the skills needed to work with relational databases effectively. You will explore topics such as table creation with constraints, indexing for performance improvement, and using stored procedures and triggers to automate and streamline database operations.

---

## Learning Objectives

By completing this project, you will learn to:

- Create and manage MySQL tables with advanced constraints.
- Optimize SQL queries using indexing to improve performance.
- Write and implement stored procedures and functions for code reuse.
- Utilize triggers to automate actions based on specific events in the database.
- Create views to simplify complex queries and enhance data abtraction.

---

## Key Concepts

This project covers the following key concepts:

- **Table Creation and Constraints**: Understanding the importance of constraints in maintaining data integrity.
- **Indexes**: Learning how to create and manage indexes to speed up data retrieval.
- **Stored Procedures**: Implementing reusable SQL code blocks for repetitive tasks.
- **Triggers**: Automating tasks in the database in response to specific events.
- **Views**: Creating virtual tables to encapsulate complex queries.

---

## Tasks

The project consists of several tasks, each focused on a specific aspect of advanced MySQL usage. Below are the tasks included in this project:

0. **We are all unique** - `0-uniq_users.sql`: Create a `users` table with unique email attribute.
1. **In and not out** - `1-country_users.sql`: Create a `users` table with country enumeration.
2. **Best band ever!** - `2-fans.sql`: A script that ranks country origins of bands by number of fans.
3. **Old school band** - `3-glam_rock.sql`: A script that lists all Glam rock bands ranked by longevity.
4. **Buy buy buy** - `4-store.sql`: A script that creates a trigger to decrease quantity after new order.
5. **Email validation** - `5-valid_email.sql`: A script that creates a trigger to reset "valid_email" when email changes.
6. **Add bonus** - `6-bonus.sql`: A script that creates a procedure to add a bonus for a student.
7. **Average score** - `7-average_score.sql`: A script that creates a procedure to compute and store the average score for a user.
8. **Optimize simple search** - `8-index_my_namees.sql`: A script that creates an index on the first letter of the name.
9. **Optimize search and score** - `9-index_name_score.sql`: A script that creates an index on the first letter of the name and score.
10. **Safe divide** - `10-div.sql`: A script that creates a function SafeDiv to safely divide two numbers.
11. **No table for a meeting** - `11-need_meeting.sql`: A script that creates a view that lists students needing a meeting.
12. **Average weighted score** - `100-average_weighted_score.sql`: A script that creates a procedure to compute average weighted score for a user.
13. **Average wighted score for all!** - `101-average_weighted_score.sql`: A script that creates a procedure to compute average weighted score for all users.

---

## Installation

To set up your environment for this project, ensure you have MySQL installed. You can install MySQL on Ubuntu with the following command:

```bash
sudo apt update
sudo apt install mysql-server
```

Make sure to secure your MySQL installation:

```bash
sudo mysql_secure_installation
```

You can start the MySQL service with:

```bash
sudo service mysql start
```

---

## Usage

Each task is provided as an individual SQL script. To execute a script, use the following command in your terminal:

```bash
mysql -u root -p < script_name.sql
```

_Replace `script_name.sql` with the name of the SQL file you wish to execute. Make sure you are connected to the correct database before running the scripts._

---

## Requirements

- **MySQL Server**: Version 5.7 ir higher.
- **Operating System**: Ubuntu 18.04 LTS or later.
- **Knowledge**: Basic understanding of SQL and relational database concepts.

---

## Author

Refiloe Radebe (_kweenDev_)

---

_This project is part of the ALX Software Engineering program, aimed at enhancing skills in backend database management and advanced SQL usage._
