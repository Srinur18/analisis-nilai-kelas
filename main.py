from pathlib import Path

from src.input_data import baca_data
from src.proses import analisis_nilai
from src.output import tampilkan_hasil, simpan_hasil


BASE_DIR = Path(__file__).resolve().parent
FILE_INPUT = BASE_DIR / "data" / "contoh_data.txt"
FILE_OUTPUT = BASE_DIR / "output" / "rekap_nilai.txt"


def main():
    print("=" * 50)
    print("          PROGRAM ANALISIS NILAI KELAS")
    print("=" * 50)

    try:
        data_mahasiswa = baca_data(FILE_INPUT)

        if not data_mahasiswa:
            print("Tidak ada data mahasiswa yang dapat dianalisis.")
            return

        hasil = analisis_nilai(data_mahasiswa)

        tampilkan_hasil(hasil)

        simpan_hasil(hasil, FILE_OUTPUT)

        print("\nRekap nilai berhasil disimpan.")
        print(f"Lokasi file: {FILE_OUTPUT}")

    except FileNotFoundError:
        print("\nError: File data tidak ditemukan.")
        print("Pastikan file data/contoh_data.txt tersedia.")

    except ValueError as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()