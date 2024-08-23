
todos=[
{"id":"1",
"activity":"jogging for 2 hours at 7:00 am"},
{"id":"2",
 "activity":"write 3 pages of new note book"},
{"id":"3",
"activity":"playing the mario game"}
]
for todo in todos:
    print(todo)
    if int((todo["id"])) == 2:
        todos.remove(todo)
print(todos)

     
