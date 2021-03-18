import requests

BASE = "http://127.0.0.1:5000/"


# test post

    # song table
response = requests.post(BASE + "addaudio/song", json={"id":1, "name":"abcr", "duration":150 })
print(response.json())

    # song already exist
response = requests.post(BASE + "addaudio/song", json={"id":1, "name":"abcr", "duration":150 })
print(response.json())

    # podcast table
response = requests.post(BASE + "addaudio/podcast", json={"id":1, "name":"abc", "duration":150, "host":"jhjhjv", "participant_1":"hjjaewav", "participant_2":"hjjjghv", "participant_3":"hgvhvh", "participant_4":"hjjvfzez", "participant_5":"hjjvre", "participant_6":"hjjvdds", "participant_7":"hhgccjjv", "participant_8":"hjjveesfe", "participant_9":"hjjvhgcg", "participant_10":"jhhjjv" })
print(response.json())

    # podcast already exist
response = requests.post(BASE + "addaudio/podcast", json={"id":1, "name":"abc", "duration":150, "host":"jhjhjv", "participant_1":"hjjaewav", "participant_2":"hjjjghv", "participant_3":"hjjvesewa", "participant_4":"hjjvfzez", "participant_5":"hjjvre", "participant_6":"hjjvdds", "participant_7":"hhgccjjv", "participant_8":"hjjveesfe", "participant_9":"hjjvhgcg", "participant_10":"jhhjjv" })
print(response.json())

    # audiobook table
response = requests.post(BASE + "addaudio/audiobook", json={"id":1, "title":"abc", "author":"jbkjb", "narrator":"hgchc", "duration":200 })
print(response.json())

    # audiobook already exist
response = requests.post(BASE + "addaudio/audiobook", json={"id":1, "title":"abc", "author":"jbkjb", "narrator":"hgchc", "duration":200 })
print(response.json())

# wrong adress
response = requests.post(BASE + "addaudio/auiobook", json={"name":"abc", "duration":150 })
print(response.json())

# test get song
response = requests.get(BASE + "audio/song/1")
print(response.json())

# test get podcast
response = requests.get(BASE + "audio/podcast/1")
print(response.json())

# test get audiobook
response = requests.get(BASE + "audio/audiobook/1")
print(response.json())

# test get not found
response = requests.get(BASE + "audio/song/10")
print(response.json())

# test get all song
response = requests.get(BASE + "audio/song")
print(response.json())

# test get all podcast
response = requests.get(BASE + "audio/podcast")
print(response.json())

# test get all audiobook
response = requests.get(BASE + "audio/audiobook")
print(response.json())

# test get all not found
response = requests.get(BASE + "audio/sog")
print(response.json())

# test update song
response = requests.put(BASE + "audio/song/1", json={"id":"1", "name":"jhjb", "duration":250 })
print(response.json())

# test update song (data not found)
response = requests.put(BASE + "audio/song/10", json={"id":"1", "name":"jhjb", "duration":250 })
print(response.json())

# test Delete song
response = requests.delete(BASE + "audio/song/1")
print(response.json())

# test update audiobook
response = requests.put(BASE + "audio/audiobook/1",json={"id":1, "title":"ajbjbc", "author":"jkjbkjb", "narrator":"hgjhbjchc", "duration":250 })
print(response.json())

# test update audiobook (data not found)
response = requests.put(BASE + "audio/audiobook/10",json={"id":1, "title":"ajbjbc", "author":"jkjbkjb", "narrator":"hgjhbjchc", "duration":250 })
print(response.json())

# test Delete audiobook
response = requests.delete(BASE + "audio/audiobook/1")
print(response.json())

# test update podcast
response = requests.put(BASE + "audio/podcast/1", json={"id":2, "name":"abc", "duration":150, "host":"jhjhjv", "participant_1":"hjjaewav", "participant_2":"hjjjghv", "participant_3":"hgvhvh", "participant_4":"hjjvfzez", "participant_5":"hjjvre", "participant_6":"hjjvdds", "participant_7":"hhgccjjv", "participant_8":"hjjveesfe", "participant_9":"hjjvhgcg", "participant_10":"jhhjjv" })
print(response.json())

# test update podcast (data not found)
response = requests.put(BASE + "audio/podcast/10", json={"id":2, "name":"abc", "duration":150, "host":"jhjhjv", "participant_1":"hjjaewav", "participant_2":"hjjjghv", "participant_3":"hgvhvh", "participant_4":"hjjvfzez", "participant_5":"hjjvre", "participant_6":"hjjvdds", "participant_7":"hhgccjjv", "participant_8":"hjjveesfe", "participant_9":"hjjvhgcg", "participant_10":"jhhjjv" })
print(response.json())

# test Delete podcast
response = requests.delete(BASE + "audio/podcast/1")
print(response.json())

# test Delete song (data not found)
response = requests.delete(BASE + "audio/song/10")
print(response.json())

# test Delete podcast (data not found)
response = requests.delete(BASE + "audio/podcast/10")
print(response.json())

# test Delete audiobook (data not found)
response = requests.delete(BASE + "audio/audiobook/10")
print(response.json())