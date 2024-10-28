# Question 1: Write a query that will display results
import mysql.connector

mydb=mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="password",
    database="racedb",
    auth_plugin="mysql_native_password"
)

mycursor=mydb.cursor()
#mycursor.execute("CREATE TABLE races ( race_id INT AUTO_INCREMENT PRIMARY KEY, race_year INT, race_name VARCHAR(255), race_date DATE, circuit_location VARCHAR(255), driver_name VARCHAR(255), driver_number INTEGER, driver_nationality VARCHAR(255), team VARCHAR(255), grid INTEGER, fastest_lap INTEGER, race_time TIME, points INTEGER, created_date DATETIME)")

# sql="INSERT INTO races(race_year,race_name,race_date,circuit_location, driver_name,driver_number,driver_nationality,team,grid,fastest_lap,race_time,points,created_date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

# races = [
#     (2017, "Australian Grand Prix", "2017-03-26", "Melbourne", "Sebastian Vettel", 5, "German", "Ferrari", 1, 67, "1:24:11", 25, "2017-03-26"),
#     (2018, "British Grand Prix", "2018-07-08", "Silverstone", "Lewis Hamilton", 44, "British", "Mercedes", 1, 62, "1:27:21", 25, "2018-07-08"),
#     (2019, "Japanese Grand Prix", "2019-10-13", "Suzuka", "Valtteri Bottas", 77, "Finnish", "Mercedes", 1, 65, "1:25:34", 26, "2019-10-13"),
#     (2020, "Portuguese Grand Prix", "2020-10-25", "Portimao", "Lewis Hamilton", 44, "British", "Mercedes", 1, 63, "1:29:56", 26, "2020-10-25"),
#     (2021, "Monaco Grand Prix", "2021-05-23", "Monaco", "Max Verstappen", 33, "Dutch", "Red Bull", 1, 64, "1:38:56", 25, "2021-05-23"),
#     (2022, "Brazilian Grand Prix", "2022-11-13", "São Paulo", "George Russell", 63, "British", "Mercedes", 1, 61, "1:39:09", 26, "2022-11-13"),
#     (2023, "Italian Grand Prix", "2023-09-03", "Monza", "Charles Leclerc", 16, "Monegasque", "Ferrari", 2, 60, "1:20:12", 18, "2023-09-03"),
#     (2024, "Canadian Grand Prix", "2024-06-16", "Montreal", "Carlos Sainz", 55, "Spanish", "Ferrari", 1, 58, "1:33:22", 25, "2024-06-16"),
#     (2019, "French Grand Prix", "2019-06-23", "Le Castellet", "Lewis Hamilton", 44, "British", "Mercedes", 1, 64,"1:24:18", 25, "2019-06-23"),
#     (2020, "Turkish Grand Prix", "2020-11-15", "Istanbul", "Lewis Hamilton", 44, "British", "Mercedes", 6, 58, "1:42:19",25, "2020-11-15")
# ]
#
# mycursor.executemany(sql, races)
# mydb.commit()

sql="SELECT * FROM races WHERE race_year=%s ORDER BY points DESC"
mycursor.execute(sql, (2020, ))
results=mycursor.fetchall()
for row in results:
    print(row)
print("done")


# Question 2: Write a python function that checks whether a word or phrase is palindrome or not
Word=input("Enter word: ")
Joined_Word=Word.replace(" ","")
print(Joined_Word)
Inverted_Word=Joined_Word[::-1]
if Inverted_Word == Joined_Word:
    print("palindrome")
else:
    print("Not palindrome")
print("done")

# Question 3: Write a python function to check whether a string is pangram or not.
import string

Word_Or_Sentence=input("Enter a word or sentence: ")
Alphabet=string.ascii_lowercase
status=set()
for i in Alphabet:
    if i in Word_Or_Sentence.lower():
        status.add("present")
    else:
        status.add("absent")
if "absent" in status:
    print("Not Pangram")
else:
    print("Pangram")
print("done")

# Question 4: Write a program that takes an integer as input and returns an integer with reversed digit ordering.
Value=int(input("Enter value: "))
if Value < 0:
    Absolute_Value=abs(Value)
    Reversed_Value="-" + str(Absolute_Value)[::-1]
    Reversed_Integer_Value=int(Reversed_Value)
    print(Reversed_Integer_Value)
else:
    Reversed=str(Value)[::-1]
    Reversed_Integer_Value=int(Reversed)
    print(Reversed_Integer_Value)
print("done")

# Question 5: Write a program that accepts a  string as input, capitalizes the first letter of each word in the string, and then returns the result string.
Sentence=input("Enter preferred statement: ")
Split_Sentence=Sentence.split(" ")
Capitalized_Array=[]

for i in Split_Sentence:
    Capitalized=i.capitalize()
    Capitalized_Array.append(Capitalized)
print(" ".join(Capitalized_Array))
print("done")