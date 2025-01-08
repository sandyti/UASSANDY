from django.db import models

class Kamar(models.Model):
    nomor_kamar = models.CharField(max_length=10)
    tipe_kamar = models.CharField(max_length=50)
    harga_per_malam = models.DecimalField(max_digits=10, decimal_places=2)
    status_ketersediaan = models.BooleanField(default=True)

    def __str__(self):
        return f"Kamar {self.nomor_kamar} - {self.tipe_kamar}"

class Tamu(models.Model):
    nama = models.CharField(max_length=100)
    kontak = models.CharField(max_length=15)
    alamat = models.TextField()

    def __str__(self):
        return self.nama

class Pemesanan(models.Model):
    kamar = models.ForeignKey(Kamar, on_delete=models.CASCADE)
    tamu = models.ForeignKey(Tamu, on_delete=models.CASCADE)
    tanggal_check_in = models.DateField()
    tanggal_check_out = models.DateField()
    total_biaya = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pemesanan {self.id} oleh {self.tamu.nama}"

class Pembayaran(models.Model):
    pemesanan = models.OneToOneField(Pemesanan, on_delete=models.CASCADE)
    tanggal_pembayaran = models.DateField()
    metode_pembayaran = models.CharField(max_length=50)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Selesai', 'Selesai')],
    )

    def __str__(self):
        return f"Pembayaran {self.pemesanan.id} - {self.status}"
