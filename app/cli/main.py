import argparse
from app.services.wallet_service import WalletService


def main():
    parser = argparse.ArgumentParser(
        description="Bitcoin Wallet Generator (Educational Only)"
    )

    parser.add_argument(
        "--testnet",
        action="store_true",
        help="Generate wallet for Bitcoin Testnet",
    )

    args = parser.parse_args()

    wallet = WalletService.create_wallet(testnet=args.testnet)

    print("\n⚠️ EDUCATIONAL PROJECT - DO NOT USE WITH REAL FUNDS\n")
    print("Mnemonic:")
    print(wallet["mnemonic"])

    print("\nAddress:")
    print(wallet["address"])

    print("\nxPub:")
    print(wallet["xpub"])


if __name__ == "__main__":
    main()
