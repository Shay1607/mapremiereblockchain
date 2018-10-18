import hashlib
import datetime

#on organise d'abord la data de notre block

class blockchain:
    def __init__(self,previous_blockchain_hash, data, timestamp):
        self.previous_blockchain_hash = previous_blockchain_hash
        self.data = data     
        self.timestamp = timestamp
        self.hash = self.get_hash()

#on crée ensuite le block d'origine

    @staticmethod
    def create_genesis_block():
        return blockchain("0","0",datetime.datetime.now())

#on crée notre première fonction de hashage

    def get_hash(self):
        header_bin=(str(self.previous_blockchain_hash)+
                    str(self.data) + 
                    str(self.timestamp)).encode()

        inner_hash = hashlib.sha256(header_bin).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash