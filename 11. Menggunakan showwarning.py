import warnings

def custom_showwarning(message, category, filename, lineno, file=None, line=None):
    print(f"Custom warning: {message}")

warnings.showwarning = custom_showwarning

def custom_warning():
    warnings.warn("Peringatan kustom menggunakan showwarning.", UserWarning)

custom_warning()
# Fungsi: Mengganti fungsi default untuk menampilkan peringatan kustom.
# Kondisi: Ketika Anda ingin mengubah cara peringatan ditampilkan secara keseluruhan.