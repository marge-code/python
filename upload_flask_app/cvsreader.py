import logging

logger = logging.getLogger('upload-app')

class CvsProductsReader:
    def __init__(self, stream):
        self.stream = stream
        self.separator = '\t'
        self.field_names = self.get_field_names()

    def get_field_names(self):
        first_line = self.stream.readline()
        return first_line.split(self.separator)

    def get_product(self):
        line = self.stream.readline()
        logger.info('parse next record')
        if not line:
            return None
        fields = line.split(self.separator)
        item = zip(self.field_names, fields)
        db_row = dict(item)
        return db_row