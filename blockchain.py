from blockchain import blockchain
import datetime

#on crée notre liste avec le premier block (connu sous le nom de genesis block, qui est
# le block d'origine)

premiere_blockchain = [blockchain.create_genesis_block()]

print("le block genesis a ete cree!")
print("Hash:%s" % premiere_blockchain[-1].hash)

#on va creer par ex 10 blocks, chaque nouveau block est ajouté au dernier

num_blocks_to_add = 10

for i in range(1,num_blocks_to_add+1):
    premiere_blockchain.append(blockchain(premiere_blockchain[-1].hash,
                            "DATA!",
                            datetime.datetime.now()))
    
    print("Block #%d a ete cree" % i)
    print("Block #%d hash: %s" % (i, premiere_blockchain[i].hash))