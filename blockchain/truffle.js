/*
 * NB: since truffle-hdwallet-provider 0.0.5 you must wrap HDWallet providers in a 
 * function when declaring them. Failure to do so will cause commands to hang. ex:
 * ```
 * mainnet: {
 *     provider: function() { 
 *       return new HDWalletProvider(mnemonic, 'https://mainnet.infura.io/<infura-key>') 
 *     },
 *     network_id: '1',
 *     gas: 4500000,
 *     gasPrice: 10000000000,
 *   },
 */

var HDWalletProvider = require("truffle-hdwallet-provider");
const MNEMONIC = "chapter mushroom smooth capable interest marriage slush agree long ill sand frown";


module.exports = {
  // See <http://truffleframework.com/docs/advanced/configuration>
  // to customize your Truffle configuration!
   networks: {
    development: {
      host: "127.0.0.1",
      port: 9545,
      network_id: "*" // Match any network id
    },
    ropsten:{
	 	provider: function() {
	 		return new HDWalletProvider(MNEMONIC, "https://ropsten.infura.io/v3/613e792e8a704ba1a4e370cf1236e24f")
	 	},
	 	network_id: 3,
	 	gas: 4000000
	  },
    kovan:{
	 	provider: function() {
	 		return new HDWalletProvider(MNEMONIC, "https://kovan.infura.io/v3/613e792e8a704ba1a4e370cf1236e24f")
	 	},
	 	 network_id: 42,
	      gas: 4700000
	  }
  }

};
