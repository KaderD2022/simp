;                (function() {
                    window.require(["ace/ext/error_marker"], function(m) {
                        if (typeof module == "object" && typeof exports == "object" && module) {
                            module.exports = m;
                        }
                    });
                })();

                (function ($) {
                    $(function () {
                
                        //initialize all modals           
                        $('.modal').modal();
                
                        //now you can open modal from code
                        $('#modal1').modal('open');
                
                        //or by click on trigger
                        $('.trigger-modal').modal();
                
                    }); // end of document ready
                })(jQuery); // end of jQuery name space