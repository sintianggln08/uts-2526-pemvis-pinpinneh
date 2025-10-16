#!/usr/bin/env python3
"""
Autograder untuk UTS Pemrograman Visual 2526
Memeriksa keberadaan file dan memberikan feedback kepada mahasiswa
"""

import os
import sys
from datetime import datetime

def print_header():
    """Print header autograder"""
    print("=" * 60)
    print("🤖 AUTOGRADER UTS PEMROGRAMAN VISUAL 2526")
    print("=" * 60)
    print(f"⏰ Waktu check: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

def check_file_exists(filename):
    """Check if file exists and return status"""
    if os.path.exists(filename):
        print(f"✅ {filename} - DITEMUKAN")
        return True
    else:
        print(f"❌ {filename} - TIDAK DITEMUKAN")
        return False

def test_faktorial():
    """Test faktorial implementation"""
    expected = {5: 120, 0: 1, 3: 6, 1: 1, 4: 24}
    print("\n📝 SOAL 1: Faktorial Rekursif")
    print("-" * 40)
    
    exists = check_file_exists("faktorial.fprg")
    if not exists:
        print("⚠️  Upload file faktorial.fprg untuk mendapatkan nilai!")
        return False
    
    print("\n🧪 Test Cases:")
    for n, exp in expected.items():
        print(f"   Input: {n} → Expected Output: {exp}")
    
    print("✨ Tips: Gunakan rekursi dengan base case n=0 atau n=1")
    return True

def test_fibonacci_sum():
    """Test fibonacci sum implementation"""
    expected = {5: 12, 7: 33, 6: 20, 4: 7}
    print("\n📝 SOAL 2: Jumlah Deret Fibonacci")
    print("-" * 40)
    
    exists = check_file_exists("fibonacci_sum.fprg")
    if not exists:
        print("⚠️  Upload file fibonacci_sum.fprg untuk mendapatkan nilai!")
        return False
    
    print("\n🧪 Test Cases:")
    for n, exp in expected.items():
        print(f"   Input: {n} → Expected Sum: {exp}")
    
    print("✨ Tips: Gunakan loop untuk menghitung dan menjumlahkan deret")
    return True

def test_nilai_analisis():
    """Test nilai analisis implementation"""
    print("\n📝 SOAL 3: Analisis Nilai Mahasiswa")
    print("-" * 40)
    
    exists = check_file_exists("nilai_analisis.fprg")
    if not exists:
        print("⚠️  Upload file nilai_analisis.fprg untuk mendapatkan nilai!")
        return False
    
    print("\n🧪 Test Case:")
    print("   Input: [80, 70, 90, 60]")
    print("   Expected Output:")
    print("     - Rata-rata = 75")
    print("     - Tertinggi = 90") 
    print("     - Terendah = 60")
    
    print("✨ Tips: Gunakan array dan loop untuk analisis data")
    return True

def test_bilangan_prima():
    """Test bilangan prima implementation"""
    print("\n📝 SOAL 4: Bilangan Prima")
    print("-" * 40)
    
    exists = check_file_exists("bilangan_prima.fprg")
    if not exists:
        print("⚠️  Upload file bilangan_prima.fprg untuk mendapatkan nilai!")
        return False
    
    print("\n🧪 Test Cases:")
    print("   Input: 10 → Expected: 2 3 5 7")
    print("   Input: 15 → Expected: 2 3 5 7 11 13")
    
    print("✨ Tips: Buat fungsi isPrima(x) terpisah untuk modularitas")
    return True

def test_kalkulator():
    """Test kalkulator implementation"""
    print("\n📝 SOAL 5: Kalkulator Sederhana")
    print("-" * 40)
    
    exists = check_file_exists("kalkulator.fprg")
    if not exists:
        print("⚠️  Upload file kalkulator.fprg untuk mendapatkan nilai!")
        return False
    
    print("\n🧪 Test Cases:")
    print("   Menu: 1 (tambah), Input: 5+3 → Expected: 8")
    print("   Menu: 2 (kurang), Input: 10-4 → Expected: 6") 
    print("   Menu: 3 (kali), Input: 4*5 → Expected: 20")
    print("   Menu: 4 (bagi), Input: 15/3 → Expected: 5")
    
    print("✨ Tips: Gunakan switch-case atau if-else untuk menu")
    return True

def generate_report(results):
    """Generate final report"""
    print("\n" + "=" * 60)
    print("📊 LAPORAN HASIL CHECK")
    print("=" * 60)
    
    total_files = len(results)
    found_files = sum(results.values())
    
    print(f"📁 Total file yang harus diupload: {total_files}")
    print(f"✅ File yang sudah diupload: {found_files}")
    print(f"❌ File yang belum diupload: {total_files - found_files}")
    
    completion = (found_files / total_files) * 100
    print(f"📈 Progress: {completion:.1f}%")
    
    if completion == 100:
        print("\n🎉 SELAMAT! Semua file sudah terupload!")
        print("💡 Pastikan untuk test flowchart sebelum deadline")
    else:
        print(f"\n⚠️  Masih ada {total_files - found_files} file yang belum diupload!")
        print("📋 File yang belum diupload:")
        for filename, exists in results.items():
            if not exists:
                print(f"   - {filename}")
    
    print("\n🔔 Reminder:")
    print("   - Test semua flowchart sebelum submit")
    print("   - Pastikan nama file sesuai spesifikasi")
    print("   - Deadline: Sesuai jadwal yang ditentukan")
    print("=" * 60)

def main():
    """Main function"""
    print_header()
    
    # Run all tests and collect results
    results = {}
    results["faktorial.fprg"] = test_faktorial()
    results["fibonacci_sum.fprg"] = test_fibonacci_sum()
    results["nilai_analisis.fprg"] = test_nilai_analisis()
    results["bilangan_prima.fprg"] = test_bilangan_prima()
    results["kalkulator.fprg"] = test_kalkulator()
    
    # Generate final report
    generate_report(results)
    
    # Return exit code based on completion
    if all(results.values()):
        sys.exit(0)  # All files found
    else:
        sys.exit(1)  # Some files missing

if __name__ == "__main__":
    main()
