# state_capital
Learn the usage of dictionary and MySQL module by implementing a simple state-capital quiz game

There are 4 different versions. All 4 are using 3 questions ("california - sacramento", "nevada - carson city" and "washington - olympia")

## 1st version
Hard coded state capital pairs in the question and answer

## 2nd version
Now the names of state and capital are stored in two different arrays. Simpler and more manageable than the 1st

## 3rd version
Now use a single dictionary to manage state and capital pairs More manageable than the 2nd one

## 4th version
Now reading from MySQL (this can be one in your laptop or a RDS in AWS). Here are SQLs used to populate MySQL accordingly

create table test.state_capital (
    state varchar(32),
    capital varchar(64)
);

insert into test.state_capital value ("California", "Sacramento");
insert into test.state_capital value ("Nevada", "Carson City");
insert into test.state_capital value ("Washington", "Olympia");
