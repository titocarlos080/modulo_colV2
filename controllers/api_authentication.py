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

        user = request.env['res.users'].sudo().search([('login', '=', username)], limit=1)
        if not user or not user._check_credentials(password):
            return request.make_response(json.dumps({'error': 'Credenciales inválidas'}), status=401)

        # Generar un token único
        token = str(uuid.uuid4())

        # Almacenar el token en la base de datos
        auth_token = request.env['auth.token'].sudo().create({
            'user_id': user.id,
            'token': token
        })

        return request.make_response(json.dumps({'token': token}), headers={'Content-Type': 'application/json'})

    @http.route('/odoo/auth/logout', auth='public', methods=['POST'], csrf=False)
    def logout(self, **kwargs):
        token = kwargs.get('token')

        if not token:
            return request.make_response(json.dumps({'error': 'Token de autenticación requerido'}), status=400)

        auth_token = request.env['auth.token'].sudo().search([('token', '=', token)], limit=1)
        if not auth_token:
            return request.make_response(json.dumps({'error': 'Token de autenticación inválido'}), status=401)

        auth_token.unlink()

        return request.make_response(json.dumps({'message': 'Sesión cerrada exitosamente'}), headers={'Content-Type': 'application/json'})
