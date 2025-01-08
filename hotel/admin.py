from django.contrib import admin
from .models import Kamar, Tamu, Pemesanan, Pembayaran
from unfold.admin import ModelAdmin

@admin.register(Kamar)
class KamarAdmin(ModelAdmin):
    list_display = ('nomor_kamar', 'tipe_kamar', 'harga_per_malam', 'status_ketersediaan')
    list_filter = ('status_ketersediaan', 'tipe_kamar')
    search_fields = ('nomor_kamar', 'tipe_kamar')

@admin.register(Tamu)
class TamuAdmin(ModelAdmin):
    list_display = ('nama', 'kontak', 'alamat')
    search_fields = ('nama', 'kontak')

@admin.register(Pemesanan)
class PemesananAdmin(ModelAdmin):
    list_display = ('kamar', 'tamu', 'tanggal_check_in', 'tanggal_check_out', 'total_biaya')
    list_filter = ('tanggal_check_in', 'tanggal_check_out')
    search_fields = ('tamu__nama', 'kamar__nomor_kamar')

@admin.register(Pembayaran)
class PembayaranAdmin(ModelAdmin):
    list_display = ('pemesanan', 'tanggal_pembayaran', 'metode_pembayaran', 'status')
    list_filter = ('status', 'metode_pembayaran')
    search_fields = ('pemesanan__id',)
