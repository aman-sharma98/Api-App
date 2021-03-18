from api_app import app
from api_app.dbconnect import connection
from flask import jsonify, request


# for create API 
@app.route('/addaudio/<audioFileType>', methods=['Post'])

def create(audioFileType):
    if request.method == 'POST':
        audio_data = request.get_json()
        c, conn = connection()

        # for song
        if audioFileType == 'song':
            # check if already exist
            data = c.execute("SELECT * FROM song WHERE id= %s", [audio_data['id']])
            if data:
                 return jsonify({"message": 'song with this id alredy exist' })

            # create and return
            c.execute("INSERT INTO song (id, name, duration) VALUES (%s, %s, %s)", 
                        (audio_data['id'], audio_data['name'], audio_data['duration']))

            conn.commit()
            c.close()
            conn.close()
        
            return jsonify({"audioFileType": audioFileType, "id":audio_data['id'], "name":audio_data['name'], "duration":audio_data['duration'] })
        
        # for podcast
        elif audioFileType == 'podcast':
            # check if already exist
            data = c.execute("SELECT * FROM podcast WHERE id= %s", [audio_data['id']])
            if data:
                 return jsonify({"message": 'podcast with this id alredy exist' })
            
            # create and return
            c.execute("INSERT INTO podcast (id, name, duration, host) VALUES (%s, %s, %s, %s)", 
                        (audio_data['id'], audio_data['name'], audio_data['duration'], audio_data['host']))
            
            c.execute("INSERT INTO participants (id, participant_1, participant_2, participant_3, participant_4, participant_5, participant_6, participant_7, participant_8, participant_9, participant_10) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (audio_data['id'], audio_data['participant_1'], audio_data['participant_2'], audio_data['participant_3'], audio_data['participant_4'], audio_data['participant_5'], audio_data['participant_6'], audio_data['participant_7'], audio_data['participant_8'], audio_data['participant_9'], audio_data['participant_10']))

            conn.commit()
            c.close()
            conn.close()
            
            return jsonify({"audioFileType": audioFileType, "id":audio_data['id'], "name":audio_data['name'], "duration":audio_data['duration'], "host":audio_data['host'], "participant_1":audio_data['participant_1'],  "participant_2":audio_data['participant_2'], "participant_3":audio_data['participant_3'], "participant_4":audio_data['participant_4'], "participant_5":audio_data['participant_5'], "participant_6":audio_data['participant_6'], "participant_7":audio_data['participant_7'], "participant_8":audio_data['participant_8'], "participant_9":audio_data['participant_9'], "participant_10":audio_data['participant_10'] })

        # for audiobook
        elif audioFileType == 'audiobook':
            # check if already exist
            data = c.execute("SELECT * FROM audiobook WHERE id= %s", [audio_data['id']])
            if data:
                 return jsonify({"message": 'audiobook with this id alredy exist' })

            # create and return
            c.execute("INSERT INTO audiobook (id, title, author, narrator, duration) VALUES (%s, %s, %s, %s, %s)", 
                        (audio_data['id'], audio_data['title'], audio_data['author'], audio_data['narrator'], audio_data['duration']))

            conn.commit()
            c.close()
            conn.close()

            return jsonify({"audioFileType": audioFileType, "id":audio_data['id'], "title":audio_data['title'], "author":audio_data['author'], "narrator":audio_data['narrator'], "duration":audio_data['duration'] })

        else:
             return jsonify({"message": 'audioFileType not found' })

        

# for get API
@app.route('/audio/<audioFileType>/<audioFileId>', methods=['GET'])

def get(audioFileType, audioFileId):
    if request.method == 'GET':
        c, conn = connection()

        # for song
        if audioFileType == 'song':
            data = c.execute("SELECT * FROM song WHERE id= %s", [audioFileId])
            if not data:
                return jsonify({'message': 'audio not found'})

            audio= c.fetchmany(data)
            audio_file = []
            
            audio_file.append({'id':audio[0][0], 'name':audio[0][1], 'duration':audio[0][2], 'upload_time':audio[0][3]})

            return jsonify({'song': audio_file})

        # for podcast
        elif audioFileType == 'podcast':
            data = c.execute("SELECT * FROM podcast WHERE id= %s", [audioFileId])
            if not data:
                return jsonify({'message': 'audio not found'})

            audio= c.fetchmany(data)
            audio_file = []
            
            audio_file.append({'id':audio[0][0], 'name':audio[0][1], 'duration':audio[0][2], 'upload_time':audio[0][3], 'host':audio[0][4]})

            return jsonify({'podcast': audio_file})

        # for audiobook
        elif audioFileType == 'audiobook':
            data = c.execute("SELECT * FROM audiobook WHERE id= %s", [audioFileId])
            if not data:
                return jsonify({'message': 'audio not found'})

            audio= c.fetchmany(data)
            audio_file = []
            
            audio_file.append({'id':audio[0][0], 'title':audio[0][1], 'author':audio[0][2], 'narrator':audio[0][3], 'duration':audio[0][4], "upload_time":audio[0][5]})

            return jsonify({'audiobook': audio_file})

        else:
             return jsonify({"message": 'audioFileType not found' })

# for get all files from category
@app.route('/audio/<audioFileType>', methods=['GET'])

def get_all(audioFileType):
    if request.method == 'GET':
        c, conn = connection()

        #for song
        if audioFileType == 'song':
            data = c.execute("SELECT * FROM song")
            if not data:
                return jsonify({'message': 'audio not found'})

            audio= c.fetchmany(data)
            all_file = []
            for i in range(0, data):
                all_file.append({'id':audio[i][0], 'name':audio[i][1], 'duration':audio[i][2], 'upload_time':audio[i][3]})

            return jsonify({'song': all_file})

        #for podcast
        elif audioFileType == 'podcast':
            data = c.execute("SELECT * FROM podcast")
            if not data:
                return jsonify({'message': 'audio not found'})

            audio= c.fetchmany(data)
            all_file = []
            for i in range(0, data):
                all_file.append({'id':audio[i][0], 'name':audio[i][1], 'duration':audio[i][2], 'upload_time':audio[i][3], 'host':audio[i][4]})

            return jsonify({'podcast': all_file})

        #for audiobook
        elif audioFileType == 'audiobook':
            data = c.execute("SELECT * FROM audiobook")
            if not data:
                return jsonify({'message': 'audio not found'})

            audio= c.fetchmany(data)
            all_file = []
            for i in range(0, data):
                all_file.append({'id':audio[i][0], 'title':audio[i][1], 'author':audio[i][2], 'narrator':audio[i][3], 'duration':audio[i][4], "upload_time":audio[i][5]})

            return jsonify({'audiobook': all_file})
        
        else:
             return jsonify({"message": 'audioFileType not found' })
    

@app.route('/audio/<audioFileType>/<audioFileId>', methods=['PUt', 'DELETE'])

def update(audioFileType, audioFileId):
    
    c, conn = connection()

    # for song
    if audioFileType == 'song':
        data = c.execute("SELECT * FROM song WHERE id= %s", [audioFileId])

        # for Update Api song
        if request.method == 'PUT':
            
            audio_data = request.get_json()

            if data:
                c.execute("UPDATE song SET id= %s, name= %s, duration= %s WHERE id= %s", 
                            (audio_data['id'], audio_data['name'], audio_data['duration'], [audioFileId]))

                conn.commit()
                c.close()
                conn.close()

                return jsonify({"id":audio_data['id'], "name":audio_data['name'], "duration":audio_data['duration'] })

            else:
                return jsonify({"message":'Data not found, unable to update' })


        # for DELETE Api song
        elif request.method == 'DELETE':
            
            if data:
                c.execute("DELETE FROM song WHERE id= %s",[audioFileId])

                conn.commit()
                c.close()
                conn.close()

                return jsonify({"message":'Data deleted, Succesfully' })

            else:
                return jsonify({"message":'Data not found, unable to delete' })


        else:
            return jsonify({"message":'invalid request' })




    # for podcast
    elif audioFileType == 'podcast':
        data = c.execute("SELECT * FROM podcast WHERE id= %s", [audioFileId])

        # for Update Api
        if request.method == 'PUT':
            
            audio_data = request.get_json()

            if data:
                c.execute("UPDATE podcast SET name= %s, duration= %s, host= %s WHERE id= %s", 
                            (audio_data['name'], audio_data['duration'], audio_data['host'], [audioFileId]))
                c.execute("UPDATE participants SET participant_1= %s, participant_2= %s, participant_3= %s, participant_4= %s, participant_5= %s, participant_6= %s, participant_7= %s, participant_8= %s, participant_9= %s, participant_10= %s WHERE id= %s", 
                            (audio_data['participant_1'], audio_data['participant_2'], audio_data['participant_3'], audio_data['participant_4'], audio_data['participant_5'], audio_data['participant_6'], audio_data['participant_7'], audio_data['participant_8'], audio_data['participant_9'], audio_data['participant_10'], [audioFileId]))

                conn.commit()
                c.close()
                conn.close()

                return jsonify({"id":audio_data['id'], "name":audio_data['name'], "duration":audio_data['duration'], "host":audio_data['host'], "participant_1":audio_data['participant_1'],  "participant_2":audio_data['participant_2'], "participant_3":audio_data['participant_3'], "participant_4":audio_data['participant_4'], "participant_5":audio_data['participant_5'], "participant_6":audio_data['participant_6'], "participant_7":audio_data['participant_7'], "participant_8":audio_data['participant_8'], "participant_9":audio_data['participant_9'], "participant_10":audio_data['participant_10'] })

            else:
                return jsonify({"message":'Data not found, unable to update' })


        # for DELETE Api
        elif request.method == 'DELETE':

            data_p = c.execute("SELECT * FROM participants WHERE id= %s", [audioFileId])
            if data and data_p:
                c.execute("DELETE FROM participants WHERE id= %s",[audioFileId])
                c.execute("DELETE FROM podcast WHERE id= %s",[audioFileId])

                return jsonify({"message":'Data deleted, Succesfully' })

            elif data:
                c.execute("DELETE FROM podcast WHERE id= %s",[audioFileId])

                conn.commit()
                c.close()
                conn.close()

                return jsonify({"message":'Data deleted, Succesfully' })

            else:
                return jsonify({"message":'Data not found, unable to delete' })

        else:
            return jsonify({"message":'invalid request' })        





    # for audiobook
    elif audioFileType == 'audiobook':
        data = c.execute("SELECT * FROM audiobook WHERE id= %s", [audioFileId])

        # for Update Api audiobook
        if request.method == 'PUT':
            
            audio_data = request.get_json()

            if data:
                c.execute("UPDATE audiobook SET id= %s, title= %s, author= %s, narrator= %s, duration= %s WHERE id= %s", 
                            (audio_data['id'], audio_data['title'], audio_data['author'], audio_data['narrator'], audio_data['duration'], [audioFileId]))

                conn.commit()
                c.close()
                conn.close()

                return jsonify({"id":audio_data['id'], "title":audio_data['title'], "author":audio_data['author'], "narrator":audio_data['narrator'], "duration":audio_data['duration'] })

            else:
                return jsonify({"message":'Data not found, unable to update' })


        # for DELETE Api audiobook
        elif request.method == 'DELETE':
            
            if data:
                c.execute("DELETE FROM audiobook WHERE id= %s",[audioFileId])

                conn.commit()
                c.close()
                conn.close()

                return jsonify({"message":'Data deleted, Succesfully' })

            else:
                return jsonify({"message":'Data not found, unable to delete' })

        else:
            return jsonify({"message":'invalid request' })

    else:
        return jsonify({"message":'invalid datatype' })


