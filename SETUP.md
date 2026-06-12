# 🚀 Setup Cepat - Jadwal Bola di GitHub Pages

## Langkah 1: Siapkan Repository

Pilih salah satu metode:

### Metode A: GitHub Desktop (Paling Mudah)
1. Download [GitHub Desktop](https://desktop.github.com)
2. Login dengan GitHub account
3. Klik **File** → **New Repository**
4. Nama: `jadwal-bola`
5. Pilih folder lokal (bisa di mana saja)
6. Klik **Create Repository**
7. Klik **Publish Repository** (pastikan Public)

### Metode B: Command Line
```bash
# Buat folder baru
mkdir jadwal-bola
cd jadwal-bola

# Init git
git init
git config user.name "Your Name"
git config user.email "your@email.com"

# Buat repository di https://github.com/new
# Kemudian set remote
git remote add origin https://github.com/USERNAME/jadwal-bola.git
git branch -M main
```

## Langkah 2: Copy File

Copy semua file dari folder `jadwal-bola-online` ke repository lokal Anda:
- `index.html`
- `README.md`
- Folder `data/` (dengan `jadwal.json`)
- Folder `.github/` (opsional, untuk auto-update)
- Folder `scripts/` (opsional, untuk auto-update)

## Langkah 3: Push ke GitHub

### Pakai GitHub Desktop:
1. Klik tombol **Current Branch** → **New Branch**
2. Di tab **Changes**, isi summary: "Initial commit"
3. Klik **Commit to main**
4. Klik **Publish branch**

### Pakai Command Line:
```bash
git add .
git commit -m "Initial commit: Jadwal Bola streaming generator"
git push -u origin main
```

## Langkah 4: Aktifkan GitHub Pages

1. Pergi ke repository di GitHub
2. Klik **Settings**
3. Di sidebar, pilih **Pages**
4. Pilih **Source**: `main` branch
5. Folder: `/ (root)`
6. Klik **Save**
7. Tunggu ~1 menit

✅ Selesai! Link akan muncul di bawah, format: `https://USERNAME.github.io/jadwal-bola`

## Langkah 5: Test & Update

1. Buka link GitHub Pages
2. Tanggal otomatis hari ini (dari sistem)
3. Jadwal akan muncul dari `data/jadwal.json`
4. Kalau tidak muncul, tekan Ctrl+Shift+R (clear cache)

## Langkah 6: Update Jadwal (Optional)

### Opsi A: Manual (Cepat)
1. Edit file `data/jadwal.json` di GitHub web editor
2. Ubah tanggal dan pertandingan
3. Commit perubahan
4. Refresh di HP/browser (Ctrl+Shift+R)

### Opsi B: Auto Update (via GitHub Actions)
1. Folder `scripts/` harus ada dengan `update_jadwal.py`
2. Folder `.github/workflows/` harus ada dengan `update-jadwal.yml`
3. Workflow akan jalan otomatis jam 9 pagi WIB setiap hari
4. Atau trigger manual di tab **Actions** → **Update Jadwal Bola** → **Run workflow**

## 📱 Buka di HP

1. Buka GitHub Pages link (ex: `https://username.github.io/jadwal-bola`)
2. Klik menu (3 garis) → "Add to Home Screen"
3. Sekarang bisa dibuka seperti app!

## 🎨 Customize

- **Header**: Edit di sidebar saat membuka aplikasi
- **Footer**: Masukkan @username TikTok Anda
- **Tema**: Pilih dari 4 pilihan warna
- **Jadwal**: Import HTML dari Goal.com atau edit manual di `data/jadwal.json`

## ❓ Troubleshooting

### Jadwal tidak muncul?
- Tekan Ctrl+Shift+R (hard refresh)
- Cek apakah file `data/jadwal.json` ada
- Format tanggal di jadwal harus `YYYY-MM-DD`

### Video tidak bisa di-download?
- Gunakan Chrome atau Edge (bukan Firefox)
- File WebM langsung bisa upload ke TikTok
- Atau convert ke MP4 pakai Handbrake gratis

### GitHub Pages belum aktif?
- Tunggu 2-3 menit setelah setting
- Cek tab **Settings** → **Pages** → cek URL

---

**Done!** Sekarang Anda bisa mulai bikin konten TikTok dari jadwal bola. 🚀⚽
