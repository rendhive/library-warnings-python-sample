import warnings

class SampleClass:
    def method(self):
        warnings.warn("Metode ini akan dihapus di versi selanjutnya.", DeprecationWarning)

obj = SampleClass()
obj.method()
# Fungsi: Mengeluarkan peringatan sebagai bagian dari method kelas.
# Kondisi: Ketika Anda ingin memberi tahu bahwa method dalam klas tidak lagi direkomendasikan.