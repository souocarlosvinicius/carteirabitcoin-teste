from app.domain.seed_generator import SeedGenerator
from app.domain.wallet import BitcoinWallet


class WalletService:

    @staticmethod
    def create_wallet(testnet: bool = False):
        seed_generator = SeedGenerator()
        mnemonic = seed_generator.generate()

        wallet = BitcoinWallet(mnemonic, testnet)
        derived = wallet.derive()

        return {
            "mnemonic": mnemonic,
            "address": derived["address"],
            "xpub": derived["xpub"],
        }
