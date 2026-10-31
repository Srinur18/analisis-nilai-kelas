from pathlib import Path


def baca_data(lokasi_file):
    """
    Membaca data mahasiswa dari file teks.

    Format:
    Nama,Nilai

    Contoh:
    Andi,80
    Budi,75
    """

    data_mahasiswa = []

    lokasi_file = Path(lokasi_file)

    with open(lokasi_file, "r", encoding="utf-8") as file:
        for nomor_baris, baris in enumerate(file, start=1):

            baris = baris.strip()

            if not baris:
                continue

            bagian = baris.split(",")

            if len(bagian) != 2:
                raise ValueError(
                    f"Format data salah pada baris {nomor_baris}."
                )

            nama = bagian[0].strip()
            nilai_text = bagian[1].strip()

            if not nama:
                raise ValueError(
                    f"Nama mahasiswa kosong pada baris {nomor_baris}."
                )

            try:
                nilai = float(nilai_text)

            except ValueError:
                raise ValueError(
                    f"Nilai harus berupa angka pada baris {nomor_baris}."
                )

            if nilai < 0 or nilai > 100:
                raise ValueError(
                    f"Nilai harus berada pada rentang 0-100 "
                    f"pada baris {nomor_baris}."
                )

            data_mahasiswa.append({
                "nama": nama,
                "nilai": nilai
            })

    return data_mahasiswa