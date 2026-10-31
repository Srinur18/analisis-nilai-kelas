from pathlib import Path


def tampilkan_hasil(hasil):
    """
    Menampilkan hasil analisis nilai ke terminal.
    """

    print("\n" + "=" * 50)
    print("              HASIL ANALISIS NILAI")
    print("=" * 50)

    print(f"Jumlah mahasiswa : {hasil['jumlah_mahasiswa']}")
    print(f"Rata-rata nilai : {hasil['rata_rata']:.2f}")
    print(f"Nilai tertinggi : {hasil['nilai_tertinggi']}")
    print(f"Nilai terendah  : {hasil['nilai_terendah']}")
    print(f"Jumlah lulus    : {hasil['jumlah_lulus']}")
    print(f"Jumlah tidak lulus : {hasil['jumlah_tidak_lulus']}")

    print("\n" + "-" * 50)
    print("DAFTAR NILAI MAHASISWA")
    print("-" * 50)

    print(f"{'Nama':<25}{'Nilai':<10}{'Status'}")
    print("-" * 50)

    for mahasiswa in hasil["data"]:

        print(
            f"{mahasiswa['nama']:<25}"
            f"{mahasiswa['nilai']:<10.2f}"
            f"{mahasiswa['status']}"
        )

    print("=" * 50)


def simpan_hasil(hasil, lokasi_file):
    """
    Menyimpan hasil analisis ke file teks.
    """

    lokasi_file = Path(lokasi_file)

    lokasi_file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(lokasi_file, "w", encoding="utf-8") as file:

        file.write("HASIL ANALISIS NILAI KELAS\n")
        file.write("=" * 50 + "\n")

        file.write(
            f"Jumlah mahasiswa: {hasil['jumlah_mahasiswa']}\n"
        )

        file.write(
            f"Rata-rata nilai: {hasil['rata_rata']:.2f}\n"
        )

        file.write(
            f"Nilai tertinggi: {hasil['nilai_tertinggi']}\n"
        )

        file.write(
            f"Nilai terendah: {hasil['nilai_terendah']}\n"
        )

        file.write(
            f"Jumlah lulus: {hasil['jumlah_lulus']}\n"
        )

        file.write(
            f"Jumlah tidak lulus: {hasil['jumlah_tidak_lulus']}\n"
        )

        file.write("\nDAFTAR NILAI MAHASISWA\n")
        file.write("-" * 50 + "\n")

        for mahasiswa in hasil["data"]:

            file.write(
                f"{mahasiswa['nama']}, "
                f"{mahasiswa['nilai']:.2f}, "
                f"{mahasiswa['status']}\n"
            )