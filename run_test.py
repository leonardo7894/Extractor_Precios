import pytest

if __name__ == "__main__":
    print("Ejecutando pruebas de scraping...\n")
    pytest.main(["-v", "tests/test_extractor.py"])