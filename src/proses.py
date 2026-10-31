BATAS_KELULUSAN = 60


def hitung_rata_rata(data_nilai):
    """
    Menghitung rata-rata nilai mahasiswa.
    """

    if not data_nilai:
        return 0

    return sum(data_nilai) / len(data_nilai)


def tentukan_kelulusan(nilai):
    """
    Menentukan status kelulusan mahasiswa.
    """

    if nilai >= BATAS_KELULUSAN:
        return "Lulus"

    return "Tidak Lulus"


def analisis_nilai(data_mahasiswa):
    """
    Mengolah data mahasiswa dan menghasilkan statistik nilai.
    """

    if not data_mahasiswa:
        return {
            "jumlah_mahasiswa": 0,
            "rata_rata": 0,
            "nilai_tertinggi": 0,
            "nilai_terendah": 0,
            "jumlah_lulus": 0,
            "jumlah_tidak_lulus": 0,
            "data": []
        }

    daftar_nilai = [
        mahasiswa["nilai"]
        for mahasiswa in data_mahasiswa
    ]

    jumlah_lulus = 0
    jumlah_tidak_lulus = 0

    data_hasil = []

    for mahasiswa in data_mahasiswa:

        nama = mahasiswa["nama"]
        nilai = mahasiswa["nilai"]

        status = tentukan_kelulusan(nilai)

        if status == "Lulus":
            jumlah_lulus += 1

        else:
            jumlah_tidak_lulus += 1

        data_hasil.append({
            "nama": nama,
            "nilai": nilai,
            "status": status
        })

    return {
        "jumlah_mahasiswa": len(data_mahasiswa),
        "rata_rata": hitung_rata_rata(daftar_nilai),
        "nilai_tertinggi": max(daftar_nilai),
        "nilai_terendah": min(daftar_nilai),
        "jumlah_lulus": jumlah_lulus,
        "jumlah_tidak_lulus": jumlah_tidak_lulus,
        "data": data_hasil
    }