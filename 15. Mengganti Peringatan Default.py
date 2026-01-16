import warnings

def sample_function():
    warnings.warn("Peringatan: Fungsi ini tidak memiliki efek.", DeprecationWarning)

warnings.filterwarnings("error")  # Mengubah peringatan menjadi exception

try:
    sample_function()
except DeprecationWarning:
    print("DeprecationWarning telah ditangkap!")
# Fungsi: Mengubah peringatan menjadi exception untuk penanganan yang lebih ketat.
# Kondisi: Ketika Anda ingin memperlakukan peringatan sebagai kesalahan.