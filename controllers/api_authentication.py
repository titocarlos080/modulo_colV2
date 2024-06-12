import uuid,json
from odoo import http 
from odoo.http import request
from odoo.exceptions import AccessError

class AuthenticationController(http.Controller):

    @http.route('/odoo/auth/login', auth='public', methods=['POST'], csrf=False)
    def login(self, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')

        if not username or not password:
            return request.make_response(json.dumps({'error': 'Nombre de usuario y contraseña requeridos'}), status=400)

        # Buscar el usuario por correo electrónico
        user = request.env['res.partner'].sudo().search([('email', '=', username)], limit=1)
        # Generar un token único
        token = str(uuid.uuid4())
         # Actualizar el token en el usuario
        user.write({'keynotificaciones': token})

        return request.make_response(json.dumps({'token': token, 'user': user.read()}), headers={'Content-Type': 'application/json'})