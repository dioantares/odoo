from odoo import http
class Umat(http.Controller):
    @http.route('/umat/data/', website=True, auth='public')
    def umat_dataumat(self):
        return "Test"

        #return requests.render("")