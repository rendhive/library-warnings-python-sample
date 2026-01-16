import warnings

def deprecated_function():
    warnings.warn("Fungsi ini sudah tidak digunakan lagi!", DeprecationWarning)

deprecated_function()
# Fungsi: Mengeluarkan peringatan saat fungsi tidak lagi digunakan.
# Kondisi: Ketika Anda ingin memberi tahu pengguna bahwa fungsi tersebut akan dihapus di versi mendatang.