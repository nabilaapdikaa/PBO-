class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
        self.nilai = {}

    def terima_nilai(self, matakuliah, nilai):
        self.nilai[matakuliah.kode] = nilai
        print(f"Mahasiswa {self.nama} ({self.npm}) menerima nilai {nilai} untuk mata kuliah {matakuliah.nama} ({matakuliah.kode}).")

    def lihat_nilai(self):
        print(f"Nilai {self.nama} ({self.npm}):")
        for kode, nilai in self.nilai.items():
            print(f"{kode}: {nilai}")

class Dosen:
    def __init__(self, nama, nip):
        self.nama = nama
        self.nip = nip

    def input_nilai(self, mahasiswa, matakuliah, nilai):
        print(f"Dosen {self.nama} ({self.nip}) menginput nilai {nilai} untuk mahasiswa {mahasiswa.nama} ({mahasiswa.npm}) pada mata kuliah {matakuliah.nama} ({matakuliah.kode}).")
        mahasiswa.terima_nilai(matakuliah, nilai)

class MataKuliah:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama

dosen1 = Dosen("Pak Puput", "123456")
mahasiswa1 = Mahasiswa("Aura", "2215061100")
mahasiswa2 = Mahasiswa("Bintang", "2215061010")

matkul_pbo = MataKuliah("IF101", "PBO")
matkul_tbo = MataKuliah("IF102", "TBO")
matkul_ai = MataKuliah("IF103", "A.I")

dosen1.input_nilai(mahasiswa1, matkul_pbo, 85.5)
print("\n")
dosen1.input_nilai(mahasiswa2, matkul_tbo, 90.2)
print("\n")
dosen1.input_nilai(mahasiswa1, matkul_ai, 88.6)

print("\n")
mahasiswa1.lihat_nilai()
print("\n")
mahasiswa2.lihat_nilai()
