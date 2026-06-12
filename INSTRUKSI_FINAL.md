# 📋 Instruksi Upload ke GitHub Pages

Folder `jadwal-bola-online` sudah siap untuk diupload ke GitHub dan berfungsi sebagai web app online yang bisa dibuka di HP tanpa aplikasi.

## 📁 Struktur File yang Sudah Dibuat

```
jadwal-bola-online/
├── index.html                    # File utama aplikasi
├── README.md                     # Dokumentasi lengkap
├── SETUP.md                      # Panduan setup cepat
├── .gitignore                    # File yang di-ignore git
├── data/
│   └── jadwal.json              # Database jadwal bola
├── scripts/
│   └── update_jadwal.py          # Script auto-update jadwal (opsional)
└── .github/
    └── workflows/
        └── update-jadwal.yml     # GitHub Actions workflow (opsional)
```

## 🚀 3 Langkah Upload ke GitHub

### LANGKAH 1: Buat Repository Baru

1. Pergi ke https://github.com/new
2. Isi **Repository name**: `jadwal-bola` (atau nama lain)
3. Pilih **Public** (biar bisa diakses orang lain)
4. ✅ Centang "Add a README file"
5. Klik **Create repository**

### LANGKAH 2: Upload File (Pilih salah satu metode)

**METODE A - Paling Mudah (Drag & Drop)**

1. Pergi ke repository yang baru dibuat (https://github.com/USERNAME/jadwal-bola)
2. Klik tombol **Code** → pilih tab **Local**
3. Klik tombol upload icon atau drag-drop folder `jadwal-bola-online`
4. Upload semua file:
   - `index.html`
   - `data/jadwal.json`
   - `scripts/update_jadwal.py`
   - `.github/workflows/update-jadwal.yml`
   - Semua file lainnya
5. Klik **Commit changes**

**METODE B - GitHub Desktop (Recommended)**

1. Download [GitHub Desktop](https://desktop.github.com)
2. Login dengan akun GitHub
3. Klik **File** → **Clone Repository**
4. Cari repository `jadwal-bola` yang baru dibuat
5. Klik **Clone**
6. Copy file dari `jadwal-bola-online` ke folder yang di-clone
7. Buka GitHub Desktop:
   - Klik **Changes** tab
   - Summary: "Initial commit"
   - Description: "Upload jadwal bola streaming generator"
   - Klik **Commit to main**
   - Klik **Push origin**

**METODE C - Command Line**

```bash
# Clone repository
git clone https://github.com/USERNAME/jadwal-bola.git
cd jadwal-bola

# Copy semua file dari jadwal-bola-online ke sini

# Commit & push
git add .
git commit -m "Initial commit: Jadwal bola streaming generator"
git push -u origin main
```

### LANGKAH 3: Aktifkan GitHub Pages

1. Pergi ke repository (https://github.com/USERNAME/jadwal-bola)
2. Klik tab **Settings**
3. Di sidebar kiri, klik **Pages**
4. **Source**: Pilih `main` branch
5. **Folder**: Pilih `/ (root)`
6. Klik **Save**
7. Tunggu ~2 menit
8. Refresh halaman, link akan muncul di bawah seperti:
   ```
   Your site is live at https://USERNAME.github.io/jadwal-bola
   ```

## ✅ SELESAI!

Aplikasi Anda sudah live online! Anda sekarang bisa:

### 1. Buka di HP
- Buka link dari GitHub Pages
- Bookmark atau "Add to Home Screen"
- Bisa digunakan offline setelah dibuka sekali

### 2. Generate PNG
- Ganti tanggal di sidebar
- Pilih tema warna
- Tulis header dan footer (nama TikTok)
- Klik "Download PNG"
- File tersimpan otomatis

### 3. Generate Video
- Klik tab "Video"
- Atur durasi per slide (3-10 detik)
- Pilih animasi masuk
- Klik "Download WebM"
- Upload langsung ke TikTok atau convert ke MP4

### 4. Update Jadwal
**Opsi A - Manual (Cepat):**
- Edit file `data/jadwal.json` di GitHub web editor
- Ubah jadwal sesuai kebutuhan
- Commit perubahan
- Refresh di HP (Ctrl+Shift+R)

**Opsi B - Auto Update (via GitHub Actions):**
- Workflow sudah setup
- Jalan otomatis jam 9 pagi WIB setiap hari
- Atau trigger manual di tab **Actions**

## 🎯 Tips Optimal

1. **Jadwal banyak?** → Buat video dengan 5-10 pertandingan saja, lebih menarik
2. **Tema?** → Pilih yang sesuai channel TikTok Anda
3. **Waktu upload?** → Post 1-2 jam sebelum pertandingan dimulai
4. **Durasi?** → 3-5 detik per pertandingan ideal untuk TikTok
5. **Watermark?** → Selalu masukkan @username TikTok di footer

## 🆘 Troubleshooting

| Masalah | Solusi |
|---------|--------|
| Jadwal tidak muncul | Tekan Ctrl+Shift+R (clear cache) |
| GitHub Pages belum aktif | Tunggu 2-3 menit, cek ulang tab Settings |
| Video tidak bisa download | Gunakan Chrome/Edge, bukan Firefox |
| Mau edit jadwal manual | Edit `data/jadwal.json` di GitHub editor |

## 📞 Bantuan Lebih Lanjut

- Baca `README.md` untuk fitur lengkap
- Baca `SETUP.md` untuk panduan detail
- Cek folder ini untuk contoh struktur data

---

**Selamat mencoba! Semoga sukses di TikTok!** 🚀⚽📱
