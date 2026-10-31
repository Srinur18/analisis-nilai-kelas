# Test Case Analisis Nilai Kelas

## Pengujian Program

| ID | Input | Expected | Actual | Status |
|---|---|---|---|---|
| T1 | Andi,80 | Lulus | Lulus | PASS |
| T2 | Dina,60 | Lulus | Lulus | PASS |
| T3 | Eko,55 | Tidak Lulus | Tidak Lulus | PASS |
| T4 | Nilai 120 | Data ditolak | Data ditolak | PASS |
| T5 | Nilai abc | Error nilai bukan angka | Error ditampilkan | PASS |
| T6 | File tidak tersedia | FileNotFoundError ditangani | Pesan error ditampilkan | PASS |
| T7 | File kosong | Tidak ada data yang dianalisis | Pesan ditampilkan | PASS |

## Hasil Pengujian

Program berhasil membaca data, menghitung statistik, menentukan
kelulusan, dan menyimpan hasil analisis.

Validasi input juga berjalan untuk data yang tidak sesuai.