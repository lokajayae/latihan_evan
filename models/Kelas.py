from odoo import models, fields, api

class Kelas(models.Model):
    _name = 'kelas.kelas'

    nama = fields.Char(string='Nama')
    mahasiswa = fields.One2many(
        "res.partner", "kelas_id",
        domain=[("is_dosen", "=", "False")],)
    wali_kelas = kelas_id = fields.Many2one(
        comodel_name='res.partner',
        string="Wali Kelas",
        domain=[("is_dosen", "=", "True")], 
    )
    mata_kuliah = fields.Many2many('mata.kuliah', string="Mata Kuliah")