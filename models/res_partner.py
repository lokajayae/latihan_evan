from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError

class res_partner(models.Model):
    _inherit = 'res.partner'

    dob = fields.Date(
      string="Tanggal Lahir"
    )
    age = fields.Integer(
      string = "Umur",
      compute = "_compute_age",
      inverse = "_inverse_age",
      search= "_search_age",
      store = False,
      readonly = True
    )
    is_dosen = fields.Boolean(
      string="Dosen",
      default=True
    )
    kelas_id = fields.Many2one(
        comodel_name='kelas.kelas',
        string="Kelas",
    )

    @api.constrains('dob')
    def _check_dob(self) :
      today = fields.Date.today()

      for people in self :
        if people.dob and people.dob >= today :
          raise models.ValidationError (
            'Tanggal Lahir kamu salah'
          )

    @api.depends('dob')
    def _compute_age(self) :
      today = fields.Date.today()
      difference = 0

      for people in self :
        if people.dob :
          # if date of birth from a person is exist
          if people.dob.month < today.month :
            difference = 0
          elif people.dob.month == today.month :
            if people.dob.day <= today.day :
              difference = 0
            elif people.dob.day > today.day :
              difference = -1
          else :
            difference = -1

          people.age = today.year - people.dob.year + difference
        else :
          # if date of birth is not exist
          people.age = -1

    def _inverse_age(self) :
      # Not yet implemented
      return True

    def _search_age(self) :
       # Not yet implemented
       return True

    