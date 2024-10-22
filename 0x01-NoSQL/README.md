
# 0x01. NoSQL Project

## Project Overview

This project focuses on working with **NoSQL** databases, specifically **MongoDB**, using the **mongo shell** and **PyMongo**, a Python driver for MongoDB. By the end of this project, you'll have learned how to perform basic database operations, such as creating databases, inserting documents, querying, updating, and deleting records. You will also learn how to implement these operations in Python scripts.

### Learning Objectives

At the end of this project, you should be able to explain the following concepts clearly:

- What NoSQL is and its advantages
- Differences between SQL and NoSQL databases
- ACID properties and their significance in databases
- Document storage and its role in NoSQL databases
- Types of NoSQL databases and their use cases
- Querying, inserting, updating, and deleting data in MongoDB
- How to use the **mongo shell** and **PyMongo** for database operations

---

## Resources

Here are some resources that you will need during the project:

- **[NoSQL Databases Explained](https://www.mongodb.com/nosql-explained)**
- **[MongoDB with Python Crash Course](https://realpython.com/introduction-to-mongodb-and-python/)**
- **[MongoDB Shell Methods](https://docs.mongodb.com/manual/reference/method/)**
- **[Aggregation in MongoDB](https://docs.mongodb.com/manual/aggregation/)**
- **[Installing MongoDB on Ubuntu 18.04](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)**

---

## Requirements

### Environment

- **Ubuntu 18.04 LTS**
- **MongoDB v4.2**
- **Python 3.7**
- **PyMongo 3.10**

### Files and Code Requirements

- All files must be interpreted/compiled on **Ubuntu 18.04**.
- Your Python scripts must be executable using the command `#!/usr/bin/env python3` at the top of the file.
- Adhere to **pycodestyle** style (version 2.5.x).
- Each script should be documented with proper module and function-level docstrings.
- The first line of each MongoDB script should be a comment in the format `// my comment`.

---

## Project Tasks

### 0. List All Databases

- **File:** `0-list_databases`
- **Description:** Write a script that lists all databases in MongoDB.

    ```bash
    mongo < 0-list_databases
    ```

### 1. Create or Use a Database

- **File:** `1-use_or_create_database`
- **Description:** Write a script that creates or uses the database `my_db`.

    ```bash
    mongo < 1-use_or_create_database
    ```

### 2. Insert a Document

- **File:** `2-insert`
- **Description:** Insert a document with the attribute `name: "Holberton school"` into the `school` collection in `my_db`.

    ```bash
    mongo my_db < 2-insert
    ```

### 3. List All Documents

- **File:** `3-all`
- **Description:** Write a script to list all documents in the `school` collection of the database passed as a command-line option.

    ```bash
    mongo my_db < 3-all
    ```

### 4. Find Documents by Match

- **File:** `4-match`
- **Description:** Write a script that lists all documents where the `name` is "Holberton school".

    ```bash
    mongo my_db < 4-match
    ```

### 5. Count Documents

- **File:** `5-count`
- **Description:** Write a script to display the count of documents in the `school` collection.

    ```bash
    mongo my_db < 5-count
    ```

### 6. Update a Document

- **File:** `6-update`
- **Description:** Write a script to update documents where `name: "Holberton school"` by adding an `address: "972 Mission street"`.

    ```bash
    mongo my_db < 6-update
    ```

### 7. Delete Documents by Match

- **File:** `7-delete`
- **Description:** Write a script to delete all documents where `name: "Holberton school"`.

    ```bash
    mongo my_db < 7-delete
    ```

### 8. List All Documents (Python)

- **File:** `8-all.py`
- **Prototype:**

    ```python
    def list_all(mongo_collection):
        """ Lists all documents in a collection """
    ```

- **Description:** Write a Python function that lists all documents in a collection. Returns an empty list if no documents are found.

### 9. Insert a Document (Python)

- **File:** `9-insert_school.py`
- **Prototype:**

    ```python
    def insert_school(mongo_collection, **kwargs):
        """ Inserts a new document in a collection and returns its ID """
    ```

- **Description:** Write a Python function that inserts a document in the `school` collection based on provided keyword arguments. It should return the new document ID.

### 10. Change school topics (Python)

- **File:** `10-update_topics.py`
- **Prototype:**

    ```python
    def update_topics(mongo_collection, name, topics):
        """ Updates the topics of a school document based on its name """ 
    ```

- **Description:** Write a Python function that changes all topics of a school document based on the name.

### 11. Where can I learn Python? (Python)

- **File:** `11-schools_by_topic.py`
- **Prototype:**

    ```python
    def schools_by_topic(mongo_collection, topic):
        """ Retrieves the list of schools that teach a specific topic. """
    ```

- **Description:** Write a Python function that returns a list of schools that offer a specific topic.

### 12. Log stats (Python)

- **File:** `12-log_stats.py`
- **Prototype:**

    ```python
    def log_stats():
        """ Prints Nginx log statistics from MongoDB collection """
    ```

- **Description:** Write a Python script that provides some stats about Nginx logs stored in MongoDB.

### 13. Regex filter

- **File:** `100-find`
- **Description:** Write a script that lists all documents with `name` starting by `Holberton` in the collection `school`.

    ```bash
    db.school.find({ name: { $regex: 'Holberton' } })
    ```

### 14. Top students (Python)

- **File:** `101-students.py`
- **Prototype:**

    ```python
    def top_students(mongo_collection):
        """ Retrieves all students sorted by their average score """
    ```

- **Description:** Write a Python function that returns all students sorted by average score.

### 15. Log stats - new version (Python)

- **File:** `102-log_stats.py`
- **Prototype:**

    ```python
    def log_stats():
        """ Prints the top 10 of the most present IPs in the Nginx collection of the logs database """
    ```

- **Description:** Improve `12-log_stats.py` by adding a sorted list of the top 10 of the most present IPs in the Nginx collection of the `logs` database.

---

## How to Install MongoDB on Ubuntu 18.04

1. Import MongoDB GPG key:

    ```bash
    wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
    ```

2. Create a MongoDB source list file:

    ```bash
    echo "deb [arch=amd64,arm64] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
    ```

3. Update and install MongoDB:

    ```bash
    sudo apt-get update
    sudo apt-get install -y mongodb-org
    ```

4. Start the MongoDB service:

    ```bash
    sudo service mongod start
    ```

5. Verify installation:

    ```bash
    mongo --version
    ```

6. If necessary, create the MongoDB data directory:

    ```bash
    sudo mkdir -p /data/db
    ```

---

## Troubleshooting

- If you face issues with the `data/db` directory, create it manually as shown above.
- If `/etc/init.d/mongod` is missing, you can refer to the MongoDB documentation for an example file setup.

---

## Author

**Refiloe Radebe**  
*Date of creation: 21 October 2024*

**GitHub Repository:** [alx-backend-storage](https://github.com/kweenDev/alx-backend-storage)
