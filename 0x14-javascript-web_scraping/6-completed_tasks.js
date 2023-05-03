#!/usr/bin/node
// this script computes the num of tasks completed by user id

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  let data = JSON.parse(body);
  const tasksCompleted = {};
  data = data.filter(({ completed }) => completed === true);
  for (const todo of data) {
    const userId = todo.userId;
    if (tasksCompleted[userId]) {
      tasksCompleted[userId] += 1;
    } else {
      tasksCompleted[userId] = 1;
    }
  }
  console.log(tasksCompleted);
});
