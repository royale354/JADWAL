# ⚽ Jadwal Bola - Streaming Generator untuk TikTok

Aplikasi web untuk generate PNG dan video jadwal bola yang siap diupload ke TikTok. Buka langsung di HP tanpa perlu install aplikasi.

## 🎯 Fitur

- **🖼️ Export PNG** — Multiple halaman otomatis untuk jadwal banyak
- **🎬 Export WebM** — Video build-up (pertandingan muncul satu per satu)
- **🎨 4 Tema** — Purple, Royal Blue, Emerald, Crimson
- **📱 Responsive** — Bekerja sempurna di HP, tablet, desktop
- **📥 Import HTML** — Paste jadwal dari Goal.com langsung
- **🔗 Custom Footer** — Tambahin @username TikTok Anda

## 🚀 Setup GitHub Pages

### 1. Buat Repository Baru
- Pergi ke [GitHub](https://github.com/new)
- Nama repo: `jadwal-bola` (atau nama lain sesuka Anda)
- Pilih **Public**
- Klik **Create Repository**

### 2. Upload File
```bash
git clone https://github.com/USERNAME/jadwal-bola.git
cd jadwal-bola

# Copy semua file dari folder jadwal-bola-online ke sini
# (index.html, README.md, dan folder data/)

git add .
git commit -m "Initial commit: Jadwal Bola streaming generator"
git push -u origin main
```

### 3. Aktifkan GitHub Pages
- Pergi ke **Settings** → **Pages**
- Pilih **Source**: `main` branch
- Klik **Save**
- Tunggu ~1 menit, link akan muncul seperti `https://USERNAME.github.io/jadwal-bola`

### 4. Buka di HP
- Salin link dari GitHub Pages
- Buka di browser HP Anda
- Bookmark / add to home screen untuk kemudahan

## 📋 Cara Pakai

### Mode 1: Online (dari GitHub Pages)
1. Buka link GitHub Pages Anda
2. Ganti tanggal kalau perlu
3. Pilih tema
4. Edit header/footer (opsional)
5. Download PNG atau video
6. Upload ke TikTok

### Mode 2: Import dari Goal.com
1. Buka [Goal.com - Jadwal Siaran](https://www.goal.com/id/berita/jadwal-tv-siaran-langsung-sepakbola-hari-ini/1qomojcjyge9n1nr2voxutdc1n)
2. Copy-paste tabel jadwal ke file HTML
3. Upload file HTML ke aplikasi (tombol "Pilih HTML File")
4. Jadwal langsung muncul

## 📝 Update Jadwal (Optional - Manual)

Edit file `data/jadwal.json` dengan format:

```json
{
  "updated": "2026-06-12T10:00:00Z",
  "source": "https://www.goal.com/...",
  "schedules": {
    "2026-06-12": [
      {
        "kickoff": "15:30",
        "matchup": "Tim A vs Tim B",
        "home": "Tim A",
        "away": "Tim B",
        "competition": "Liga Inggris",
        "tv": "Vidio / Indosiar",
        "tvFree": ["Indosiar"],
        "tvPaid": ["Vidio"]
      }
    ]
  }
}
```

Push ke GitHub, tunggu ~1 menit, refresh browser (Ctrl+Shift+R).

## 🎥 Export Video

- **Format**: WebM (langsung bisa upload ke TikTok)
- **Durasi per slide**: 1-10 detik (default 3)
- **Kualitas**: 2500kbps (medium)
- **Ukuran file**: ~5-15MB tergantung jumlah pertandingan

### Jika ingin MP4:
- Download file WebM
- Buka [Handbrake](https://handbrake.fr) (gratis)
- Drag WebM → ubah output ke MP4
- Simpan dan selesai

## 💡 Tips TikTok

1. **Durasi ideal**: 15-60 detik per video
2. **Jadwal ideal**: 5-10 pertandingan per video
3. **Watermark**: Gunakan footer untuk @username
4. **Tema**: Pilih tema yang sesuai preferensi
5. **Upload time**: Post saat pre-match (1-2 jam sebelum pertandingan)

## 🛠️ Tech Stack

- **Frontend**: HTML5 Canvas, Vanilla JavaScript
- **Hosting**: GitHub Pages (gratis)
- **Browser Support**: Chrome, Firefox, Safari, Edge

## 📄 License

Bebas digunakan untuk keperluan pribadi dan komersial.

---

**Pertanyaan atau issue?** Buat issue di repository GitHub Anda.

Selamat membuat konten TikTok yang seru! ⚽🚀
