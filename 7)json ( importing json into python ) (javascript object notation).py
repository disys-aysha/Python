import json

x  = {"ID" : "1000"  ,
      "name|" : "john" ,
      "DOB|" : "01/01/2000"  ,
      "Gender" : "F" ,
      "Age" : 20 ,
      "Zip code" :
      "08122-2324" ,
      "Amount" : 1500.20,


      "id": "2000" ,
      "name" : "Jim McDonald" ,
      "dob" : "02/02/2020" ,
      "gender" : "M" ,
      "Age" : 25 ,
      "zipcode" : "08136-2324" ,
      "Amount" : 1500.20,

      "ID" : "20"  ,
      "name|" : "Jim McDonald" ,
      "DOB|" : "01/01/1999"  ,
      "Gender" : "M" ,
      "Age" : 25 ,
      "Zip code" : "08122-2324" ,
      "Amount" : 1500.20,

      
      
 }

y = json.loads(x)

print (y)








