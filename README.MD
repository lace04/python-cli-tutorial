# Simple CLI with Python

This is a simple CLI application that allows you to create, read, update, and delete users.

## Requirements

* Python 3.6+
* click
* json

## Installation

pip install click json

## Usage

python cli.py


The following commands are available:

* `new` - Create a new user.
* `user` - Get a user by ID.
* `delete` - Delete a user by ID.
* `update` - Update a user by ID.
* `users` - List all users.

For example, to create a new user named "John Doe", you would run the following command:

python cli.py new --name John --lastname Doe


To get a user by ID, you would run the following command:

python cli.py user 1


To delete a user by ID, you would run the following command:

python cli.py delete 1


To update a user by ID, you would run the following command:

python cli.py update 1 --name Jane --lastname Doe


To list all users, you would run the following command:

python cli.py users

