import sys
import time
import random
from rich.console import Console, Group
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.prompt import Prompt
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

# --- KONFIGURASI TEMA KALI LINUX ---
console = Console()
COLOR_HIJAU = "bold green"    # Hijau Hacker
COLOR_BIRU  = "bold blue"     # Biru Aksen
COLOR_MERAH = "bold red"      # Merah Warning / Signature
COLOR_PUTIH = "bold white"

# --- ASCII ART "FH-TOOL" (Versi Rapi & Pas di HP) ---
ASCII_BANNER = """
[bold green]
 ______ __  __  ______            _ 
|  ____|  ||  ||_   _|          | |
| |__  |  __  |  | |  ___   ___ | |
|  __| |  ||  |  | | / _ \ / _ \| |
| |    |  ||  |  | || (_) | (_) | |
|_|    |__||__|  |_| \___/ \___/|_|
[/]"""

def clear_screen():
    print("\033c", end="")

def print_banner():
    clear_screen()
    
    # 1. Membuat Objek ASCII & Info
    # Kita menggunakan Text.from_markup untuk ASCII agar warnanya terbaca
    ascii_art = Align.center(Text.from_markup(ASCII_BANNER))
    
    info_text = Align.center(Text("FiberHome Exploit Toolkit v2.5", style="white"))
    
    # 2. Menggabungkan dengan Group (Solusi Anti Error)
    # Group memungkinkan kita menumpuk elemen tanpa Text.assemble yang error
    konten_banner = Group(
        ascii_art,
        Text("\n"), # Spasi dikit
        info_text
    )
    
    # 3. Membuat Panel Utama
    console.print(Panel(
        konten_banner,
        border_style=COLOR_BIRU,
        title="[bold green]root@kali:~/fh-tool[/]",
        title_align="left",        # Judul di Kiri Atas
        subtitle="[bold red]by arulll[/]",
        subtitle_align="right",    # Signature di Kanan Bawah
        padding=(0, 1)
    ))

def loading_animation():
    """Animasi progress bar ala hacking"""
    print()
    with Progress(
        SpinnerColumn(style="red"),
        TextColumn("[bold green]{task.description}"),
        BarColumn(style="blue"),
        TextColumn("[yellow]{task.percentage:>3.0f}%"),
    ) as progress:
        task = progress.add_task("[green]Decrypting handshake...", total=100)
        while not progress.finished:
            # Simulasi kecepatan acak
            progress.update(task, advance=random.uniform(2, 5))
            time.sleep(0.05)

def generate_key(ssid):
    """Logika Simulasi: Membuat password dummy"""
    # Ambil angka dari SSID
    digits = ''.join(filter(str.isdigit, ssid))
    if not digits: digits = "1234"
    
    # Tambah akhiran acak heksadesimal
    chars = "abcdef0123456789"
    suffix = ''.join(random.choice(chars) for _ in range(4))
    
    return f"{digits}{suffix}"

def menu_crack():
    print_banner()
    
    # Panel Input Target
    console.print(Panel(
        "[grey70]Masukkan SSID Target (Contoh: [white]FH2102[/])[/]",
        title="[bold blue]TARGET SETTING[/]",
        border_style="blue",
        title_align="left"
    ))
    
    # Input Prompt Khas Kali Linux
    ssid = Prompt.ask(f" [bold green]┌──(root㉿kali)-[~/crack]\n └─# Input SSID[/]")
    
    if len(ssid) > 1:
        console.print(f"\n [cyan][*] Target initialized: {ssid}[/]")
        time.sleep(0.5)
        
        loading_animation()
        
        # Hasil Generate
        password_found = generate_key(ssid)
        
        # Tabel Hasil (Clean Style)
        tabel_hasil = Table(show_header=False, box=None, padding=(0, 1))
        tabel_hasil.add_column("Key", style="cyan")
        tabel_hasil.add_column("Val", style="bold white")
        
        tabel_hasil.add_row("SSID Name", f": {ssid}")
        tabel_hasil.add_row("Security", ": WPA2-PSK")
        tabel_hasil.add_row("Password", f": [on green bold black] {password_found} [/]")
        
        console.print(Panel(
            tabel_hasil,
            title="[bold green]CRACK SUCCESS[/]",
            border_style="green",
            title_align="left"
        ))
        
        console.print("[italic grey50]\n* Salin password di atas untuk login.[/]")
    else:
        console.print("[bold red][!] SSID tidak boleh kosong![/]")
    
    Prompt.ask("\n[bold white]Tekan Enter untuk kembali...[/]")

def show_about():
    print_banner()
    
    # Tabel Info Rapi
    tabel_info = Table(show_header=False, box=None, padding=(0, 1))
    tabel_info.add_row("[cyan]Developer[/]", ": [bold red]arulll[/]")
    tabel_info.add_row("[cyan]Team[/]", ": Termux Indonesia")
    tabel_info.add_row("[cyan]Fungsi[/]", ": Simulasi Audit FH-Router")
    tabel_info.add_row("[cyan]Versi[/]", ": 3.0 Stable")
    
    console.print(Panel(
        tabel_info,
        title="[bold blue]ABOUT[/]",
        border_style="blue",
        title_align="left"
    ))
    Prompt.ask("\n[bold white]Tekan Enter untuk kembali...[/]")

def main():
    while True:
        print_banner()
        
        # --- MENU UTAMA RATA KIRI (RAPI) ---
        # Menggunakan Table tanpa border (box=None) agar terlihat seperti list teks biasa tapi lurus
        menu_table = Table(show_header=False, box=None, padding=(0, 1))
        
        # Definisi Kolom: Kolom 1 sempit (No), Kolom 2 lebar (Deskripsi)
        menu_table.add_column("No", style="bold green", justify="left", width=6)
        menu_table.add_column("Desc", style="bold white", justify="left")
        
        # Isi Menu
        menu_table.add_row("[01]", "Start Crack WiFi (SSID Mode)")
        menu_table.add_row("[02]", "Tentang Tools / About")
        menu_table.add_row("[00]", "[red]Keluar / Exit Program[/]")
        
        # Tampilkan dalam Panel
        console.print(Panel(
            menu_table,
            title="[bold blue]MAIN MENU[/]",
            border_style="green",
            title_align="left", # Judul Menu di Kiri
            padding=(0, 1)
        ))
        
        # Input Pilihan
        choice = Prompt.ask(f" [bold green]┌──(root㉿kali)-[~/menu]\n └─# Pilih[/]", choices=["1", "2", "0", "01", "02", "00"])
        
        if choice in ["1", "01"]:
            menu_crack()
        elif choice in ["2", "02"]:
            show_about()
        elif choice in ["0", "00"]:
            console.print("\n[red]Exiting system...[/]")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Force Close.[/]")
