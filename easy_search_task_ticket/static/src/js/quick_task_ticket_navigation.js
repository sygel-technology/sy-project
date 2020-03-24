odoo.define('easy_search_task_ticket.QuickTaskTicketNavigation', function (require) {
"use strict";

var config = require('web.config');
var SystrayMenu = require('web.SystrayMenu');
var Widget = require('web.Widget');

var QuickTaskTicketNavigation = Widget.extend({
    template: 'QuickTaskTicketNavigation',
    sequence: 10,
    events: {
        'keydown .o_quick_task_ticket_id': '_onInputKeydown',
    },

    //--------------------------------------------------------------------------
    // Handlers
    //--------------------------------------------------------------------------

    /**
     * @private
     * @param {KeyEvent} ev
     */
    _onInputKeydown: function (ev) {
        if (ev.which === $.ui.keyCode.ENTER) {
            var id = parseInt(this.$('.o_quick_task_ticket_id').val());
            var model = String(this.$('.o_quick_task_ticket_type').val());
            if (!_.isNaN(id) && !_.isNaN(model)) {
                this.do_action({
                    res_id: id,
                    res_model: model,
                    target: 'current',
                    type: 'ir.actions.act_window',
                    views: [[false, 'form']],
                }).then(function (result) {
                    $('.o_quick_task_ticket_id').css('color', 'black');
                }).fail(function (result) {
                    $('.o_quick_task_ticket_id').css('color', 'red');
                });
            }
        }
    },
});
if (!config.device.isMobile) {
    SystrayMenu.Items.push(QuickTaskTicketNavigation);
}
});
