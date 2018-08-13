from peewee import *

db = PostgresqlDatabase('companyProject', host='localhost', user='postgres', password='Fuckyou31')


class Project (Model):
    name = CharField()
    type = CharField()
    start_date = DateField()
    end_date = DateField()
    amount = IntegerField()
    description = TextField()


    class Meta:
        database = db
        table_name = "Projects"
db.connect()
Project.create_table(fail_silently='true')
# print("Table Created")

# record_one = Project.create(name="project uno", type="Internal", start_date = date(2018,8,12), end_date= date(2018,11,30), amount= 1233
# print(Project.select().get().name)
#
# for project in Project.select():
#     print(project.name)
# for project in Project:
#     print(project, project.name, project.type, project.start_date,project.amount,project.end_date,project.description)

