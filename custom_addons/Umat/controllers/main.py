from odoo import http
from odoo.http import request

class Umat(http.Controller):
    @http.route('/umat/data/', auth='public', website=True)
    def umat_dataumat(self):
        # return "Test"
        return request.render("Umat.umat_page", {})

