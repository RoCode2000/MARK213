/*!
* Start Bootstrap - Modern Business v5.0.7 (https://startbootstrap.com/template-overviews/modern-business)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-modern-business/blob/master/LICENSE)
*/

// This file contains the JavaScript code to enable card expansion/collapse functionality

document.addEventListener('DOMContentLoaded', function() {
    var cards = document.querySelectorAll('.card');
    cards.forEach(function(card) {
        card.addEventListener('click', function() {
            var collapse = this.querySelector('.collapse');
            var isCollapsed = collapse.classList.contains('show');
            if (isCollapsed) {
                collapse.classList.remove('show');
            } else {
                collapse.classList.add('show');
            }
        });
    });
});


