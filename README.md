Project Notes

Planning - organised database in dbdiagram
In addition to users, require exercises, workout, routines
Routines are made up of workouts, workouts made up of exercises
Started work on backend by creating apps for each of these
at least at first, all data is personal to individual users - added authorisation so that users have to be the owner to be able to view the data. Being able to share routines is a potential later feature that could be added. Created a custom `IsOwner` permission to allow for this
at every stage, all routes were extensively tested in Postman to ensure they were behaving as intendede

next steps:
add activities!
create a set of dummy data
create relationships between data

wanted to experiment with many-to-many fields - was great to do that. workouts can contain many exercises, which can be included in many workouts. and the same with workouts and routines.