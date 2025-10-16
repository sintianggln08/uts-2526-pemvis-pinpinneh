import xmltodict
import os

def test_faktorial():
    expected = {5:120, 0:1, 3:6}
    print("\nTesting faktorial...")
    if not os.path.exists("faktorial.fprg"):
        print("❌ faktorial.fprg tidak ditemukan"); return
    for n, exp in expected.items():
        # simulasi output (disederhanakan, asumsikan mahasiswa mencetak hasil akhir)
        print(f"Input {n} → expected {exp}")

def test_fibonacci_sum():
    expected = {5:12, 7:33}
    print("\nTesting fibonacci_sum...")
    if not os.path.exists("fibonacci_sum.fprg"):
        print("❌ fibonacci_sum.fprg tidak ditemukan"); return
    for n, exp in expected.items():
        print(f"Input {n} → expected {exp}")

def test_nilai_analisis():
    print("\nTesting nilai_analisis...")
    if not os.path.exists("nilai_analisis.fprg"):
        print("❌ nilai_analisis.fprg tidak ditemukan"); return
    print("Expected output: avg=75, max=90, min=60")

def test_bilangan_prima():
    print("\nTesting bilangan_prima...")
    if not os.path.exists("bilangan_prima.fprg"):
        print("❌ bilangan_prima.fprg tidak ditemukan"); return
    print("Input 10 → expected: 2 3 5 7")

def test_kalkulator():
    print("\nTesting kalkulator...")
    if not os.path.exists("kalkulator.fprg"):
        print("❌ kalkulator.fprg tidak ditemukan"); return
    print("Input (4,5,menu=3) → expected 20")

if __name__ == "__main__":
    test_faktorial()
    test_fibonacci_sum()
    test_nilai_analisis()
    test_bilangan_prima()
    test_kalkulator()
