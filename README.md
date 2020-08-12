# Chat Challenge

A simple browser-based chat application using Python.

This application should allow several users to talk in a chatroom and also to get stock quotes from an API using a specific command.

## Features

- Allow registered users to log in and talk with other users in a chatroom.
- Allow users to post messages as commands into the chatroom with the following format: `/stock=stock_code`
- Create a ​ decoupled bot that will call an API using the stock_code as a parameter (​ https://stooq.com/q/l/?s=aapl.us&f=sd2t2ohlcv&h&e=csv​, here aapl.us is the stock_code)
- The bot should parse the received CSV file and then it should send a message back into the chatroom using a message broker like RabbitMQ. The message will be a stock quote using the following format: “APPL.US quote is $93.42 per share”. The post owner will be the bot.
- Have the chat messages ordered by their timestamps and show only the last 50 messages.
- Have more than one chatroom.
- Handle messages that are not understood or any exceptions raised within the bot.


## Installation

- python 3.6.8
- django 2.2 

## Installation

This guide is for setting up development instances. 

1. Create a virtual environment
2. Clone repository
3. Install dependencies from requirements.txt

## Usage

- Chat url: /
- User #1 user:user1 pass:chatpass1
- User #2 user:user2 pass:chatpass2
- To enter to backend got to: /admin/
- Admin user credentials are user:admin pass:jobsitychallenge
