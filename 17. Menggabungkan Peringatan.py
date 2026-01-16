import warnings

def combined_warning_example(x, y):
    if x < 0:
        warnings.warn("x adalah negatif!", UserWarning)
    if y < 0:
        warnings.warn("y adalah negatif!", UserWarning)

combined_warning_example(-1, -5)
# Fungsi: Mengeluarkan beberapa peringatan tergantung pada kondisi.
# Kondisi: Ketika Anda ingin menggabungkan beberapa kondisi peringatan dalam satu fungsi.