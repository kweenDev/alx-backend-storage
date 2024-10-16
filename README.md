# ALX Backend Storage

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Database_icon.svg/1200px-Database_icon.svg.png" width="100%" height="50%"/>

This repository contains a series of projects focused on backend storage systems, using both SQL and NoSQL databases. These projects are part of the ALX Software Engineering program, designed to teach advanced database management, query optimization, and practical database integration for backend systems.

## Table of Contents

- [Project Overview](#project-overview)
- [Learning Objectives](#learning-objectives)
- [Project List](#project-list)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Author](#author)

## Project Overview

The **alx-backend-storage** repository provides hands-on experience with both SQL and NoSQL databases. It covers a variety of advanced database topics such as creating and optimizing tables, using stored procedures and triggers, working with NoSQL databases like MongoDB, and managing key-value stores using Redis. Through these projects, developers will learn to handle complex data operations and enhance backend performance.

## Learning Objectives

By working through the projects in this repository, you will:

- Master advanced SQL techniques, including indexing, stored procedures, and triggers.
- Understand how to use NoSQL databases like MongoDB for flexible, schema-less data storage.
- Learn to manage and optimize Redis, a powerful key-value store used for caching and session management.
- Improve query performance and database design for better scalability and efficiency.
- Gain experience in integrating databases into backend systems.

## Project List

Below are the projects contained in this repository:

### 0x00. MySQL Advanced

- **Focus**: Advanced SQL database management using MySQL.
- **Key Concepts**: Creating tables, constraints, indexes, stored procedures, triggers, and views.

### 0x01. NoSQL

- **Focus**: Introduction to NoSQL databases, specifically MongoDB.
- **Key Concepts**: CRUD operations, aggregation, schema-less design, and performance optimization.

### 0x02. Redis Basic

- **Focus**: Basic operations in Redis, a NoSQL key-value store.
- **Key Concepts**: Redis data types, persistence options, and caching strategies.

---

## Installation

To get started with the projects in this repository, clone the repository to your local machine using the following command:

```bash
git clone https://github.com/<your-username>/alx-backend-storage.git
```

Navigate to a specific project directory to work on a particular project, for example:

```bash
cd alx-backend-storage/0x00-MySQL_Advanced
```

## Usage

Each project contains scripts that can be executed individually. Instructions for running these scripts are provided within each project directory. For instance:

1. **To execute a MySQL script:**

```bash
mysql -u root -p < script.sql
```

2. **To execute a MongoDB script:**

```bash
mongo < script.js
```

Ensure that the required databases (MySQL, MongoDB, or Redis) are properly installed and configured before executing the scripts.

## Requirements

- **MySQL**: Version 5.7 or higher.
- **MongoDB**: Version 4.0 or higher.
- **Redis**: Version 5.0 or higher.
- **Operating System**: Ubuntu 18.04 LTS or later.

## Author

_Refiloe Radebe_ (_kweenDev_)

_This repository is created as part of the ALX Software Engineering program._
