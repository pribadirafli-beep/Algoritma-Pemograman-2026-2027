
print("=== INPUT NILAI MAHASISWA ===")

nama = input("Nama Mahasiswa: ")
tugas = int(input("Nilai Tugas: "))
UTS = int(input("Nilai UTS: "))
UAS = int(input("Nilai UAS: "))
Kehadiran = int(input("Kehadiran (%): "))

# Menghitung nilai akhir
nilai_akhir = (
    (tugas * 0.25)
    + (UTS * 0.15)
    + (UAS * 0.15)
    + (Kehadiran * 0.45)
)

# Menentukan grade
if nilai_akhir >= 80:
    grade = "A"
elif nilai_akhir >= 70:
    grade = "B"
elif nilai_akhir >= 60:
    grade = "C"
else:
    grade = "D"

# Menyimpan data mahasiswa
data = {
    "Nama": nama,
    "Nilai Tugas": tugas,
    "Nilai UTS": UTS,
    "Nilai UAS": UAS,
    "Kehadiran": Kehadiran,
    "Nilai Akhir": nilai_akhir,
    "Grade": grade
}

# Menentukan status kelulusan
if nilai_akhir >= 60:
    data["Keterangan"] = "Lulus"
else:
    data["Keterangan"] = "Tidak Lulus"

# Menampilkan hasil
print("\n=== DATA NILAI MAHASISWA ===")
print(f"Nama Mahasiswa: {data['Nama']}")
print(f"Nilai Tugas (0-100): {data['Nilai Tugas']}")
print(f"Nilai UTS (0-100): {data['Nilai UTS']}")
print(f"Nilai UAS (0-100): {data['Nilai UAS']}")
print(f"Kehadiran (%): {data['Kehadiran']}")

print("\n=== HASIL NILAI MAHASISWA ===")
print(f"Nama Mahasiswa: {data['Nama']}")
print(f"Tugas: {data['Nilai Tugas']}")
print(f"UTS: {data['Nilai UTS']}")
print(f"UAS: {data['Nilai UAS']}")
print(f"Kehadiran: {data['Kehadiran']} %")

print("_" * 40)

print(f"Nilai Akhir: {data['Nilai Akhir']:.2f}")
print(f"Nilai Huruf: {data['Grade']}")
print(f"{'Status':<15}: {data['Keterangan']}")
