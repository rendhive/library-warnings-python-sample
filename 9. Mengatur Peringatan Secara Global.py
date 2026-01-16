import warnings

warnings.simplefilter("once")  # Mengatur semua peringatan untuk ditampilkan sekali saja

def example_once():
    warnings.warn("Peringatan yang ditampilkan hanya sekali.", UserWarning)

example_once()
example_once()  # Peringatan ini tidak akan muncul lagi
# Fungsi: Mengatur filter global untuk peringatan agar hanya muncul sekali.
# Kondisi: Ketika Anda ingin mengurangi jumlah peringatan yang ditampilkan.