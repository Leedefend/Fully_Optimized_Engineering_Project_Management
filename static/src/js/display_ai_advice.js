
odoo.define('engineering_project_management.display_ai_advice', function(require){
    "use strict";
    var core = require('web.core');
    var Dialog = require('web.Dialog');

    function renderAdvice(env, action) {
        const advice = action.params.advice;
        const content = `
            <h3>📘 项目任务结构建议</h3>
            <p>${advice["任务建议"] || advice}</p>
        `;
        new Dialog(this, {
            title: "AI建议中心",
            $content: $('<div>').html(content),
            buttons: [{text: "确定", close: true}]
        }).open();
    }

    core.action_registry.add('display_ai_advice', renderAdvice);
});
