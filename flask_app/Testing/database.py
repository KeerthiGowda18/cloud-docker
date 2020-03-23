class MongoDatabase(object):
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client.db
        self.collection = self.db.collection

    def list(self, query):
        data_list = list()
        for data in self.collection.find(query):
            data['id'] = str(data.pop('_id'))
            data = self._convert_datetime_to_str(data)
            data_list.append(data)
        return data_list

    def _convert_datetime_to_str(self, data):
        for key in data.keys():
            if isinstance(data[key], datetime.datetime):
                data[key] = data[key].strftime('%Y-%m-%dT%H:%M:%S')
        return data