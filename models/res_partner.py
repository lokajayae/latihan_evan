from odoo import models, fields, api, _
from odoo.exceptions import UserError

class res_partner(models.Model):
    _inherit = 'res.partner'

    age = fields.Integer(
      string="Umur"
    )
    is_dosen = fields.Boolean(
      string="Dosen",
      default=True
    )
    kelas_id = fields.Many2one(
        comodel_name='kelas.kelas',
        string="Kelas",
    )

    