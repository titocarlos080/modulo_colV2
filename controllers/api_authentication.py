import uuid,json
from odoo import http 
from odoo.http import request
from odoo.exceptions import AccessError

class AuthenticationController(http.Controller):
    @http.route('/odoo/auth/login', auth='public', methods=['POST'], csrf=False)
    def login(self, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')
    
        user = request.env['res.partner'].sudo().search([('email', '=', username)], limit=1)
    
        if user:
            user.keynotificaciones = str(uuid.uuid4())
            return request.make_response(json.dumps({'name': user.name, 'email': user.email,'keynotificaciones': user.keynotificaciones}), headers={'Content-Type': 'application/json'}, status=200)
        else:
            return request.make_response(json.dumps({'message': 'No existe el usuario'}), headers={'Content-Type': 'application/json'}, status=404)

            