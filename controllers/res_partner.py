from odoo import http
from odoo.http import request

class LatihanEvan(http.Controller):
    @http.route('/api/test', type='json', auth='none')
    def index(self, **kw):
        return "Hello World from Odoo API"
    
    @http.route('/api/dosen', type='json', auth='user')
    def get_dosen(self,  context=None, **kw) :
      partner = request.env['res.partner'].search([])
      dosen = []
      for item in partner :
        if item.is_dosen :
          vals = {
            'id' : item.id,
            'name' : item.name
          }
          dosen.append(vals)
      
      result = {
        'status': 200,
        'message': 'Success to get all Dosen',
        'result': dosen,
      }

      return result

    @http.route('/api/mahasiswa', type='json', auth='user')
    def get_mahasiswa(self, **kw) :
      partner = request.env['res.partner'].search([])
      mahasiswa = []
      for item in partner :
        if not item.is_dosen :
          vals = {
            'id' : item.id,
            'name' : item.name
          }
          mahasiswa.append(vals)
      
      result = {
        'status': 200,
        'message': 'Success to get all Mahasiswa',
        'result': mahasiswa,
      }

      return result

    @http.route('/api/create_dosen', type='json', auth='user')
    def create_dosen(self, **kw) :
      if request.jsonrequest :
        value = {
          'name': kw['name'],
          'is_dosen': True
        }
        new_dosen = request.env['res.partner'].sudo().create(value)
        return {
          'status': 200,
          'message': 'Success to create new Dosen',
          'result': new_dosen.id,
        }

    @http.route('/api/update_dosen', type='json', auth='user')
    def update_dosen(self, **kw) :
      if request.jsonrequest :
        value = {
          'name': kw['name']
        }
        id = int(kw['id'])
        updated_dosen = request.env['res.partner'].search([('id', '=', id)]).write(value)
        return {
          'status': 200,
          'message': 'Success to update Dosen',
        }

    @http.route('/api/delete_dosen', type='json', auth='user')
    def delete_dosen(self, **kw) :
      if request.jsonrequest :
        id = int(kw['id'])
        updated_dosen = request.env['res.partner'].search([('id', '=', id)]).unlink()
        return {
          'status': 200,
          'message': 'Success to delete Dosen',
        }
    