import warnings

def deprecated_function():
    warnings.warn("Fungsi ini mungkin akan dihapus!", DeprecationWarning)

warnings.simplefilter("always")  # Selalu tampilkan peringatan

for _ in range(2):
    deprecated_function()
# Fungsi: Mematuhi peringatan yang ditinggalkan selama eksekusi berulang.
# Kondisi: Ketika Anda ingin memastikan pengguna tidak melewatkan peringatan.