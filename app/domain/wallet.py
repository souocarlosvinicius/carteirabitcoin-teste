from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins


class BitcoinWallet:

    def __init__(self, mnemonic: str, testnet: bool = False):
        self.mnemonic = mnemonic
        self.testnet = testnet

    def derive(self):
        seed = Bip39SeedGenerator(self.mnemonic).Generate()

        coin = (
            Bip44Coins.BITCOIN_TESTNET
            if self.testnet
            else Bip44Coins.BITCOIN
        )

        wallet = Bip44.FromSeed(seed, coin)

        account = wallet.Purpose().Coin().Account(0)
        address = account.Change(False).AddressIndex(0)

        return {
            "address": address.PublicKey().ToAddress(),
            "xpub": account.PublicKey().ToExtended(),
        }
