# DOKUMENTASI APLIKASI CAKRUH (CAKRAWALA SURUH)


Selamat Datang di Dokumentasi **Aplikasi Cakruh (Cakrawala Suruh).** Dokumentasi ini Dibuat Agar Pengguna Dapat Dengan Mudah Memesan Jasa Yang Di Sediakan Oleh Cakruh.

---

## PERMASALAHAN YANG TERJADI

Belakangan ini banyak sekali mahasiswa yang pusing karena sedang banyak tugas maupun tempat yang sulit untuk dijangkau, contohnya seperti : Fotocopy. Dan karena kebingungan untuk mengakses itu mahasiswa jadi bingung untuk print tugas, print makalah dan juga skripsi.

Selain sulit untuk mencari tempat seperti fotocopy, mahasiswa juga terkadang ingin memesan makanan tetapi dikarenakan ongkir aplikasi yang mahal mahasiswa jadi malas untuk memesannya, dan akhirnya mahasiswa tersebut tidak jadi memesan makanan maupun minuman lewat aplikasi.

Selain 2 hal diatas mahasiswa juga sering kesusahan ketika terjadi masalah mendadak, seperti kendaraan yang suka tiba-tiba mogok, ban kendaraan kempes tiba-tiba, bingung ingin pergi ke suatu tempat tetapi harga pesan ojek yang begitu mahal.

Maka dari beberapa permasalahan diatas kita ber inisiatif untuk menghadirkan aplikasi jasa yaitu **Cakruh (cakrawala suruh)** kami membuat kami membuat jasa cakruh untuk mengatasi permasalahan-permasalahan mahasiswa yang terjadi dengan harga yang jauh relatif lebih murah, kami juga membuat aplikasi cakruh agar mahasiswa mudah memesan jasa cakruh dan juga di aplikasi cakruh bisa melihat pricelist jasa yang tersedia jadi bisa lebih menyesuaikan dompet mahasiswa-mahasiswa yang sedang mengalami masalah tapi tetap dengan murah dan juga mudah untuk diakses.

---

## BEBERAPA HAL YANG TIDAK BISA DILAKUKAN OLEH CAKRUH
Ada beberapa hal yang tidak bisa dilakukan oleh cakruh karena cakruh tidak menyediakan jasa berikut yaitu : 

- **Joki Tugas** : Cakruh tidak bisa melakukan joki tugas karena hal itu merupakan kecurangan, dan cakruh tidak mentoleransi apapun kecurangan.

- **Joki Skripsi** : Dikarenakan skripsi adalah tugas akhir mahasiswa maka cakruh tidak ingin mengambil resiko dengan menerima joki tugas.

- **Joki Game** : Karena cakruh berada di lingkungan mahasiswa dan tujuan cakruh adalah membantu permasalahan mahasiwa di sekitar kampus, maka cakruh tidak bersedia untuk joki game.

## Anggota Tim

|NAMA | NIM | USERNAME |
| :--- | :--- | :--- | 
| Abdul Rouf | 26110300006 | @Lubdaonly |
| Daitoryo Prabu Arena | 26110300027 | @Daitoryo |
| Muhammad Ricky Prasetyo | 26110300032 | @RickylianMbappe |

## Deliverables
* **D1. Topic & Problem Statement:** [Topic Statement](/docs/D1-Topic.md)
* **D2. Module Breakdown:** [Modules](/docs/modules)
* **D3. Use Case Diagram:** [Use Case Diagram](/docs/diagrams/img/use-case.png)
* **D4. Sequence Diagrams:** [Sequence Diagram Scenario 1](/docs/diagrams/img/sequence-scenario-01.png) [Scenario 2](/docs/diagrams/img/sequence-scenario-02.png) [Scenario 3](/docs/diagrams/img/sequence-scenario-03.png)
* **D5. Kolaborasi & Log Aktivitas:** [Activity Log](activity-log.md)
* **D6. Test Case Design:** [Table Test Case](/docs/tabel-case-test.md)
* **D7. Unit-Tested Code:** [Unit Tested Code](/src/payment_function.py)

## Struktur Repo
```
/ Cakruh-Cakrawala-Suruh
├── README.md                        # Berisi deskripsi aplikasi dan tautan
├── ACTIVITY_LOG.md                  # Log aktivitas tim
├── docs/
    └── diagrams/                    # Source code puml diagram
           └── /img                  # Gambar diagram use case dan sequence
    └── modules/                   
           └── tabel-case-test.md    # Tabel common & edge case
├── src/                   
    └── payment_function.py          # Kode fungsi utama 
    ├── pytest_payment.py            # Kode pytest 
    └── output_pytest.png            # Gambar hasil tes 
```

## Cara Menjalankan Pytest

Buka terminal di direktori proyek dan jalankan perintah :
```bash
pytest pytest_payment.py -v
```
## Penggunaan AI
- **Claude:** Digunakan untuk merancang unit untuk test case dan kode pytest, beserta membuat tabel test case.
- **Gemini:** Digunakan untuk merancang source code use case dan sequence diagram beserta scenario. Membantu revisi modul dan beberapa readme.

