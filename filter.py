#!/bin/env python3

# The 'imported data'
api = []
first = {"results":[{"gender":"male","name":{"title":"Mr","first":"Oliver","last":"Kokko"},"location":{"street":{"number":9635,"name":"Fredrikinkatu"},"city":"Haukipudas","state":"Ostrobothnia","country":"Finland","postcode":80166,"coordinates":{"latitude":"-23.2588","longitude":"-3.8895"},"timezone":{"offset":"+3:00","description":"Baghdad, Riyadh, Moscow, St. Petersburg"}},"email":"oliver.kokko@example.com","login":{"uuid":"a58f217c-e48a-46f6-a9bf-67effab83118","username":"sadwolf490","password":"mellon","salt":"7sINA0AM","md5":"8db39d50a8fed972920bb893f0eedae3","sha1":"b46c009c00690f4befa690a3719660318401e1f3","sha256":"130b731058ba7b695c58d09df5c9a14fa037f7cf360255f35fd4f6459b9e0f17"},"dob":{"date":"1972-08-27T22:58:49.876Z","age":49},"registered":{"date":"2020-07-07T16:41:37.173Z","age":2},"phone":"09-675-210","cell":"045-706-84-52","id":{"name":"HETU","value":"NaNNA187undefined"},"picture":{"large":"https://randomuser.me/api/portraits/men/94.jpg","medium":"https://randomuser.me/api/portraits/med/men/94.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/94.jpg"},"nat":"FI"}],"info":{"seed":"6050e39b27b06c2c","results":1,"page":1,"version":"1.4"}}
second = {'results': [{'gender': 'female', 'name': {'title': 'Mrs', 'first': 'Hanny', 'last': 'Schnabel'}, 'location': {'street': {'number': 6231, 'name': 'Neue Straße'}, 'city': 'Backnang', 'state': 'Bayern', 'country': 'Germany', 'postcode': 99491, 'coordinates': {'latitude': '-52.2452', 'longitude': '131.0179'}, 'timezone': {'offset': '+7:00', 'description': 'Bangkok, Hanoi, Jakarta'}}, 'email': 'hanny.schnabel@example.com', 'login': {'uuid': '6c9d9b01-fa89-4a4e-8f21-fe7ec1e01783', 'username': 'bigzebra930', 'password': 'blackdog', 'salt': 'OGLOq3W9', 'md5': '5f2f6f9d06f56e5a80a43b6eeee55fdf', 'sha1': '01503099bc5becb201fa9b660872723cbe18676b', 'sha256': '3c98aab56491dbb67b79c02936e2ccf511cf6a4a9fa8e0571428a990304e4fe6'}, 'dob': {'date': '1972-11-11T11:56:30.670Z', 'age': 49}, 'registered': {'date': '2019-12-23T20:51:20.102Z', 'age': 2}, 'phone': '0080-1451695', 'cell': '0170-8318182', 'id': {'name': 'SVNR', 'value': '10 111172 S 852'}, 'picture': {'large': 'https://randomuser.me/api/portraits/women/74.jpg', 'medium': 'https://randomuser.me/api/portraits/med/women/74.jpg', 'thumbnail': 'https://randomuser.me/api/portraits/thumb/women/74.jpg'}, 'nat': 'DE'}], 'info': {'seed': '830c46ecad2ffa78', 'results': 1, 'page': 1, 'version': '1.4'}}
third = {"results":[{"gender":"female","name":{"title":"Ms","first":"Emilie","last":"Keller"},"location":{"street":{"number":1747,"name":"Bergstraße"},"city":"Homberg (Efze)","state":"Sachsen","country":"Germany","postcode":64761,"coordinates":{"latitude":"-53.7523","longitude":"57.0476"},"timezone":{"offset":"-8:00","description":"Pacific Time (US & Canada)"}},"email":"emilie.keller@example.com","login":{"uuid":"46e2216c-9154-4584-927e-57e8bf96790b","username":"tinyfrog523","password":"jaguar1","salt":"evpwFquk","md5":"e379e112a9e8772785a43dd4bdb9bb80","sha1":"9731d1be5879fd329ed9d43982a330b576a87566","sha256":"76c3defb411e5d0ebc6f998ee5fc4fa6ceb13a3bc3ea5e1fb6d517b44912b472"},"dob":{"date":"1997-02-26T17:03:23.532Z","age":25},"registered":{"date":"2012-08-10T15:08:57.518Z","age":9},"phone":"0954-4606866","cell":"0173-6935830","id":{"name":"SVNR","value":"16 260297 K 657"},"picture":{"large":"https://randomuser.me/api/portraits/women/71.jpg","medium":"https://randomuser.me/api/portraits/med/women/71.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/women/71.jpg"},"nat":"DE"}],"info":{"seed":"2ceaf26fb123cadc","results":1,"page":1,"version":"1.4"}}
api.append(first)
api.append(second)
api.append(third)

# Sort and print data
r = "results"
uA = 0
for x in api:
 for a in api[uA][r][0]:
  for b in api[uA][r][0][a]:
   if b == "first":
    f = api[uA][r][0][a][b]
   if b == "last":
    l = api[uA][r][0][a][b]
   if a == "location" and b == "street":
    s = api[uA][r][0][a][b]["name"]
   if a == "location" and b == "street":
    n = api[uA][r][0][a][b]["number"]
   if b == "username":
    u = api[uA][r][0][a][b]
   if a == "email":
    e = api[uA][r][0][a]
   if b == "password":
    p = api[uA][r][0][a][b]
 uA = uA + 1
 print("\n\nPersonal info\nFirstname: " + f + "\nLastname: " + l + "\nStreetname: " + s + "\nStreetNr: " + str(n) + "\n\nCredentials\nUsername: " + u + "\nEmail: " + e + "\nPassword: " + p)
