from app.domain.wallet import BitcoinWallet


def test_wallet_derivation():
    mnemonic = (
        "abandon abandon abandon abandon abandon abandon "
        "abandon abandon abandon abandon abandon about"
    )

    wallet = BitcoinWallet(mnemonic)
    derived = wallet.derive()

    assert "address" in derived
    assert "xpub" in derived
