import warnings

def noisy_function():
    warnings.warn("Ini adalah peringatan kebisingan.", UserWarning)

warnings.filterwarnings("ignore")  # Mengabaikan semua peringatan

noisy_function()
# Fungsi: Menghentikan semua peringatan yang dihasilkan oleh fungsi.
# Kondisi: Ketika Anda perlu menonaktifkan output peringatan global.