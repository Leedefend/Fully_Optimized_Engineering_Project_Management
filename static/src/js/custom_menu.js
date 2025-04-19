odoo.define('your_module_name.custom_menu', function (require) {
    "use strict";

    var Menu = require('web.Menu');

    Menu.include({
        start: function () {
            this._super.apply(this, arguments);
            this.$menu_sections = this.$el.find('.o_menu_sections');
            this._bindEvents();
        },

        _bindEvents: function () {
            var self = this;
            this.$menu_sections.on('click', 'a[data-menu]', function (ev) {
                ev.preventDefault();
                var menuId = $(this).data('menu');
                self.trigger_up('menu_clicked', { id: menuId });
            });
        }
    });
});
