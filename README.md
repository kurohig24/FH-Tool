# FH-TOOL (FiberHome Exploit Toolkit)

![Python](https://img.shields.io/badge/Language-Python3-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux-green?style=for-the-badge&logo=linux)
![Status](https://img.shields.io/badge/Status-Active-red?style=for-the-badge)

**FH-TOOL** adalah alat simulasi audit keamanan jaringan untuk router FiberHome. Tools ini dirancang dengan antarmuka **CLI Modern** menggunakan library `Rich`, menampilkan animasi hacking yang realistis dan tema ala **Kali Linux**.

> **Note:** Tools ini dibuat untuk tujuan **EDUKASI** dan **SIMULASI**.

---

## 📸 Screenshot Tampilan

![Tampilan Tools](screenshot.jpg)

*Tampilan UI yang rapi dengan menu rata kiri dan ASCII Art anti-pecah.*

---

## 🔥 Fitur Utama

* [x] **Kali Linux Theme:** Tampilan hitam-hijau neon yang garang.
* [x] **Responsive ASCII Art:** Logo tidak pecah saat dibuka di HP (Portrait).
* [x] **Rich UI:** Menggunakan panel, tabel, dan warna yang rapi.
* [x] **Simulasi Cepat:** Algoritma dummy generate password yang cepat.
* [x] **No Error:** Sudah diperbaiki dari bug text alignment.

---

## 📦 Cara Install & Penggunaan

Silakan ikuti perintah di bawah ini satu per satu di terminal **Termux** atau Linux Anda.

### 1. Update & Install Dependencies
Pertama, update paket termux dan install git serta python.

```bash
pkg update && pkg upgrade -y
pkg install git python -y
pip install rich
git clone [https://github.com/kurohig24/FH-Tool.git](https://github.com/kurohig24/FH-Tool.git)
cd FH-Tool
python fh_tool_final.py
