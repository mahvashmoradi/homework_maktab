"""
This code is written by group 5 maktab 51. It's connect to database and create tables and calculate some queries.
"""
import psycopg2


def insert_country(country_list):
    """
    insert country list to "country" table
    :param country_list: list of country
    :return: nothing
    """
    cursor.executemany("""insert into country(name)
                        values (%s)""", country_list)


def insert_province(province_list):
    """
    insert province list to "province" table
    :param province_list: list of province
    :return: nothing
    """
    cursor.executemany("""insert into province(name,country_id)
                        values (%s,%s)""", province_list)


def insert_city(city_list):
    """
    insert city list to "city" table
    :param city_list: list of city
    :return:nothing
    """
    cursor.executemany("""insert into city(name,province_id)
                                values (%s,%s)""", city_list)


def insert_airport(airport_list):
    """
    insert airport list to "airport" table
    :param airport_list:list of airport
    :return: nothing
    """
    cursor.executemany("""insert into airport(name,city_id,longitude,latitude)
                                values (%s,%s,%s,%s)""", airport_list)


def insert_airline(airline_list):
    """
    insert airline list to "airline" table
    :param airline_list: list of airline
    :return: nothing
    """
    cursor.executemany("""insert into airline(name)
                    values (%s)""", airline_list)


def insert_flight(flight_list):
    """
    insert flight list to "flight" table
    :param flight_list: list of flight
    :return: nothing
    """
    cursor.executemany("""insert into flight(f_date,source_id,destination_id,f_time,airline_id,
                    flight_no,latest_price,latest_capacity)
                    values (%s,%s,%s,%s,%s,%s,%s,%s)""", flight_list)


def insert_price_capacity(price_capacity_list):
    """
    insert information of price_capacity to "price_capacity" table
    :param price_capacity_list: list of price_capacity information
    :return: nothing
    """
    cursor.executemany("""insert into price_capacity(flight_id,date_,time_,price,capacity)
    values(%s,%s,%s,%s,%s)""", price_capacity_list)


# create connection
try:
    connection1 = psycopg2.connect(host='127.0.0.1', user='maktab_user', password='123456',
                                   dbname='Airline_ticketing2')
    cursor = connection1.cursor()
except Exception as e:
    print(e)

cursor.execute("""create table country(
                id serial not null primary key,
                name varchar(40) not null)""")
cursor.execute("""create table province(
                id serial not null primary key,
                name varchar(40) not null,
                country_id int not null,
                constraint c1 foreign key (country_id) references country (id))""")
cursor.execute("""create table city(
                id serial not null primary key,
                name varchar(40) not null,
                province_id int not null,
                constraint c2 foreign key(province_id) references province(id))""")
cursor.execute("""create table airport(
                id serial not null primary key,
                name varchar(40) not null,
                city_id int not null,
                longitude int,
                latitude int,
                constraint c3 foreign key(city_id) references city(id))""")
cursor.execute("""create table airline(
                id serial not null primary key,
                name varchar(40) not null)""")
cursor.execute("""create table flight(
                id serial not null primary key,
                f_date date not null,
                source_id int not null,
                destination_id int not null,
                f_time int not null,
                airline_id int not null,
                flight_no varchar(20) not null,
                latest_price int,
                latest_capacity int,
                constraint c4 foreign key(source_id) references airport(id),
                constraint c5 foreign key(destination_id) references airport(id),
                constraint c6 foreign key(airline_id) references airline(id))""")
cursor.execute("""create table price_capacity(
                flight_id int not null,
                date_ date,
                time_ int,
                price int not null,
                capacity int not null,
                constraint c7 foreign key (flight_id) references flight(id))""")
connection1.commit()
country_list = [("Iran",), ("America",), ("Dubai",), ("France",)]
province_list = [("Tehran", 1), ("Isfahan", 1), ("Yazd", 1), ("Tabriz", 1),
                 ("California", 2), ("Boston", 2), ("Nevada", 2),
                 ("Jumeirah", 3), ("Abu Dhabi", 3),
                 ("Paris", 4), ("Monaco", 4)]
city_list = [("Tabriz", 4), ("Kashan", 2), ("Karaj", 1), ("Tehran", 1), ("Los Angeles", 5),
             ("Los Vegas", 7), ("Alsharjeh", 9), ("Isfahan", 2)]
airport_list = [("Mehrabad", 4, 10, 20), ("Imam Khomeini", 4, 20, 30), ("Shahid Sadoughi", 3, None, None),
                ("JF Kennedi", 5, 13, 15), ("John Hopkins", 6, 10, 10), ("Payam", 3, 34, 35),
                ("Isfahan", 8, 20, 20)]
airline_list = [("Lufthansa",), ("Emirates",), ("Qatar Airways",), ("Turkish Air",), ("Iran Air",), ("Qeshm Air",)]

flight_list = [("1400-03-23", 1, 5, 12, 3, "ps752", 240, 24),
               ("1400-03-23", 4, 2, 20, 1, "ps453", 100, 1),
               ("1400-03-23", 6, 5, 2, 6, "as123", 20, 0),
               ("1400-03-20", 6, 5, 3, 6, "as124", 10, 0),
               ("1400-03-20", 7, 1, 4, 5, "as564", 5, 9),
               ("1400-03-10", 1, 4, 17, 4, "ps765", 300, 8)]

price_capacity_list = [(1, "1400-03-22", 20, 260, 40),
                       (1, "1400-03-23", 14, 245, 27),
                       (1, "1400-03-23", 18, 240, 24),
                       (2, "1400-03-19", 10, 300, 100),
                       (2, "1400-03-19", 12, 200, 50),
                       (2, "1400-03-19", 19, 290, 80),
                       (2, "1400-03-20", 11, 200, 20),
                       (2, "1400-03-20", 17, 100, 1),
                       (6, "1400-03-09", 20, 400, 100),
                       (6, "1400-03-09", 22, 350, 80),
                       (6, "1400-03-10", 9, 310, 30),
                       (6, "1400-03-09", 10, 300, 8)]

insert_country(country_list)
connection1.commit()
insert_province(province_list)
connection1.commit()
insert_city(city_list)
connection1.commit()
insert_airport(airport_list)
connection1.commit()
insert_airline(airline_list)
connection1.commit()
insert_flight(flight_list)
connection1.commit()
insert_price_capacity(price_capacity_list)
connection1.commit()

print("1-Airlines with the most number of flights: ")
cursor.execute("""select name,count(*) as c
                    from airline a join flight b on a.id=b.airline_id
                    group by name
                    order by c desc
                    limit 1
                    """)
data = cursor.fetchall()
# print(data)
categorize = lambda x: 'not active' if x[1] == 0 else 'active' if (0 < x[1] <= 5) else 'highly active'
airline_categorize = [[airline[0], categorize(airline)] for airline in data]
print(airline_categorize)

print("\n2-All flights between Tehran and Isfahan: ")
cursor.execute("""
                    select *
                    from flight
                    where source_id
                    in (
                    select id from airport where city_id in(
                    select id
                    from city
                    where name='Isfahan' or name='Tehran')) and
                    destination_id in(
                    select id from airport where city_id in(
                    select id
                    from city
                    where name='Isfahan' or name='Tehran'))""")
print(cursor.fetchall())
# question 2 with other solution
# cursor.execute(
#             """select f.id
#             from flight f inner join airport a1 on f.source_id=a1.id
#             inner join airport a2 on f.destination_id=a2.id
#             inner join city c1 on c1.id=a1.city_id
#             inner join city c2 on c2.id=a2.city_id
#             where c1.name in ('Tehran','Isfahan') and c2.name in ('Tehran','Isfahan')
#               ;""")
# print(cursor.fetchall())
print("\n3-Find the a date with the most number of flights. As an example on 1 Khordad 1400 we have 1000 flights"
      " have been done:")
cursor.execute("""
                    select f_date,count(*) c
                    from flight
                    group by f_date
                    order by c desc
                    limit 1""")
print(cursor.fetchall())
print("\n4-Flights which their destination is Tehran.:")
cursor.execute(
    """
        select *
        from flight
        where
        destination_id in(
        select id from airport where city_id=(
        select id
        from city
        where name='Tehran'))""")
print(cursor.fetchall())
# question 4 with other solution
# cursor.execute(
#                 """select *
#                 from flight f inner join airport a on f.destination_id= a.id
#                 inner join city c on a.city_id=c.id
#                 where c.name='Tehran';""")
# print(cursor.fetchall())
print("\n5-List all international flights: ")
"""solving question 5 with logic:flight which source or destination country is not iran """
cursor.execute("""select * from public.flight where source_id in(
                    select id from airport where city_id in
                    (select id
                    from city
                    where province_id in(select id from province where country_id in
                                         (select id from country where name!='Iran'))))
                    or destination_id in(select id from airport where city_id in
                    (select id
                    from city
                    where province_id in(select id from province where country_id in
                                         (select id from country where name!='Iran'))))
                    """)
print(cursor.fetchall())
"""solving question 5 with another logic: flights in which source country id different from destination country"""
# cursor.execute(
#                 """select *
#                 from flight f inner join airport a1 on f.source_id=a1.id
#                 inner join airport a2 on f.destination_id=a2.id
#                 inner join city c1 on c1.id=a1.city_id
#                 inner join city c2 on c2.id=a2.city_id
#                 inner join province p1 on p1.id=c1.province_id
#                 inner join province p2 on p2.id=c2.province_id
#                 inner join country co1 on co1.id=p1.country_id
#                 inner join country co2 on co2.id=p2.country_id
#                 where co1.id!=co2.id""")
# print(cursor.fetchall())
print("\n6-Find a flight which it’s price is more than average of all flight prices:")
cursor.execute("""select * from flight
                    where latest_price > (select avg(latest_price) as total_average
                    from flight)
                    """)
print(cursor.fetchone())
