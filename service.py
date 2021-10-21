from flask import request
import json
from config import mongo_client
from bson.objectid import ObjectId
from bson.json_util import dumps

class Todo:
    coll_name = 'todo'

    def __init__(self):
        pass

    def get(self):
        user_id = request.headers.get('userid')
        response = []
        for data in mongo_client[self.coll_name].find({'user_id': user_id}):
            data['_id'] = str(data['_id'])
            response.append(data)
        return response

    def create(self):
        user_id = request.headers.get('userid')
        data = request.get_json(force=True)
        data['user_id'] = user_id
        data['_id'] = str(mongo_client[self.coll_name].insert(data))
        return data
    
    def update(self, todo_id):
        user_id = request.headers.get('userid')
        data = request.get_json(force=True)
        data['user_id'] = user_id
        mongo_client[self.coll_name].update_one({'_id': ObjectId(todo_id), 'user_id': user_id}, {'$set': data})
        return data
    
    def delete(self, todo_id):
        user_id = request.headers.get('userid')
        mongo_client[self.coll_name].delete_one({'user_id': user_id, '_id': ObjectId(todo_id)})
        return True