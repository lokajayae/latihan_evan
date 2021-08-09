from odoo import models, fields, api

class MataKuliah(models.Model):
    _name = 'mata.kuliah'

    kode = fields.Char(string='Kode Mata Kuliah')
    nama = fields.Char(string='Nama Mata Kuliah')
    kelas_ids = fields.Many2many('kelas.kelas', string="Kelas")
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Dosen Pengampu',
        domain=[("is_dosen", "=", "True")],
    )
    image = fields.Binary(
        string="Foto"
    )