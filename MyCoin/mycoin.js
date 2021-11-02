//indicate the required packages 
const SHA256 = require("crypto-js/sha256");
/*
block class contain the template of a single block 
this can be the block transaction history
block position in the hole chain, time created, previous block's hash and transaction information
*/
class BlockCrypto {
  constructor(index, current_time, info, previousHash = " ") {
    this.index = index;
    this.current_time = current_time;
    this.info = info;
    this.previousHash = previousHash;
    this.hash = this.computeHash();
     }

  computeHash() {
    return SHA256(
      this.index +
        this.previousHash +
        this.current_time +
        JSON.stringify(this.info)
          ).toString();
  }
   block_info(informaton){
this.info=informaton
  }
}
/*
Blockchain class is the template for the whole blockchain system
It governs the interctions between blocks in the chain 
Mantains the authenticity of the whole block chain and any required validations 
It should also governs the process of adding new blocks alocating them in the desired location 
The class has an hardcoded chain to act as the first block in the chain 
All the other blocks originate from the hardcoded chain 
*/
class Blockchain {
  constructor() {
    this.block1chain = [this.initGenesisBlock()];
    this.difficulty = 4;
  }
  initGenesisBlock() {
    return new BlockCrypto(0, "06/04/2021", "Initial Block in our network", "0");
  }

  obtainLatestBlock() {
    return this.block1chain[this.block1chain.length - 1];
  }
  addNewBlock(newBlock) {
    newBlock.previousHash = this.obtainLatestBlock().hash;
    newBlock.hash = newBlock.computeHash();
        this.block1chain.push(newBlock);
  }

  checkChainValidity() {
    for (let i = 1; i < this.block1chain.length; i++) {
      const currentBlock = this.block1chain[i];
      const previousHash = this.block1chain[i - 1];

      if (currentBlock.hash !== currentBlock.computeHash()) {
        return this.block1chain[i].index;
      }
      if (currentBlock.previousHash !== previousHash.hash) return this.block1chain[i].index;
    }
    return true;
  }
  /**
   * more fucntions should be added to validate the mining process using the difficulty provided 
   */
}
/*
*This section tests the blockchain functions by adding blocks and varifying authenticity 
*/
let mycoin = new Blockchain();

console.log("Adding new blocks....");
mycoin.addNewBlock(
  block1=new BlockCrypto(1, "06/04/2021", {
    sender: "James Kinywa",
    recipient: "Eve Wafula",
    quantity: 20
  })
);

mycoin.addNewBlock(
  block2=new BlockCrypto(2, "07/04/2022", {
    sender: "Anita Vyona",
    recipient: "Felix Mush",
    quantity: 349
  })
);
block1.block_info({
    sender: "The Guy",
    recipient: "Felix Mush",
    quantity: 33
  })
 
console.log(mycoin.checkChainValidity())
console.log(JSON.stringify(mycoin, null, 4));