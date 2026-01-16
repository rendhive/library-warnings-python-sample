import warnings

def multiple_warnings():
    warnings.warn("Pertama!", UserWarning)
    warnings.warn("Kedua!", UserWarning)

multiple_warnings()
# Fungsi: Mengeluarkan beberapa peringatan berturut-turut.
# Kondisi: Ketika Anda memiliki beberapa kondisi yang perlu diperingati.