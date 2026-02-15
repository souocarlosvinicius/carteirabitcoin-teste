from app.domain.seed_generator import SeedGenerator


def test_seed_generation():
    generator = SeedGenerator()
    mnemonic = generator.generate()

    assert isinstance(mnemonic, str)
    assert len(mnemonic.split()) == 12
