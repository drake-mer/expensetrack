
$(function(){
    var globalAjaxSettings = {
      async: false,
      accepts: 'json'
    }

    $('#datetimepicker1').datetimepicker();
    $("#alert_not_logged").hide();

    var globalDebug = function(){
        $('#debug_window').append("<p class='debug_message'>GLOBAL: "+JSON.stringify(GLOBAL_STATE)+"</p>\n");
    }

    var httpDebug = function(){
        if (LAST_HTTP_ANSWER){
            $('#debug_window').append("<p class='debug_message'>HTTP: " + LAST_HTTP_ANSWER +"</p>\n");
        } else {
            $('#debug_window').append("<p class=\"debug_message\">HTTP: " + LAST_HTTP_ANSWER + "</p>\n");
        }

    }

    var debug = function(){
        if (GLOBAL_STATE.debug){
            globalDebug(); httpDebug();
        }
    }

    var is_logged = function(){
        return GLOBAL_STATE.logged;
    }

    GLOBAL_STATE = {
        /* Strong convention to be followed:
        ** Only the init_page() function may modify this object
        ** Other method can read it for convenience but should never be used to set fields values
        ** When the global state has to be changed, one has to call init_page() with adequate
        ** parameters.
        */
        logged: false,
        admin: false,
        username: null,
        password: null,
        token: null,
        url: "http://localhost:8000",
        auth_route: "api-token-auth",
        user_route: "users",
        record_route: "records",
        debug: true
    }

    LAST_HTTP_ANSWER = null;

    var init_page = function(username, logged, token){
        GLOBAL_STATE.logged=logged;
        GLOBAL_STATE.token=token;
        if ( (!logged) || (!token) ){
            $('#loggout_form').hide();
            $('#logging_form').show();
            GLOBAL_STATE.username=null;
        } else {
            $('#loggout_form').show();
            $('#logging_form').hide();
            if (username){
                GLOBAL_STATE.username=username;
            }
        }
        debug();
    }
    init_page('david', true, "b4a8a313eb062dbff8c7b9cfee28e9bcfddb9dc8");

    // ajax requests
    var sendAuthenticationRequest = function(url, username, password){

        var auth_callback = function(data, status){
            init_page('', status=='success', data.token);
        }
        /* perform AJAX request */
        LAST_HTTP_ANSWER = $.post( url, { username: username, password: password }, auth_callback );
    }

    var sendListRecordsRequest = function(url, token){
        var user_list_callback = function(data, status){
            /* this callback function processes the API results */
            LAST_HTTP_ANSWER = data;
            debug();
        }
        /* perform AJAX request */
        $.ajax(url, {
            type: 'GET',
            // dataType: 'json',
            headers: { "Authorization": "Token " + token },
            processData: false,
            success: user_list_callback,
        });
    }

    var sendListUsersRequest = function(url, token){
        var user_list_callback = function(data, status){
            /* this callback function processes the API results */
            LAST_HTTP_ANSWER = data;
            debug();
        }
        /* perform AJAX request */
        $.ajax(url, {
            type: 'GET',
            headers: { "Authorization": "Token " + token },
            processData: false,
            success: user_list_callback,
        });
    }

    var showNotLoggedWarning=function(){
        $('#alert_not_logged').show()
    }

    // User events
    $("#clean_debug_cross").click( function(){
        $(".debug_message").empty();
    });

    $("#hide_not_logged_warning").click( function(){
        $("#alert_not_logged").hide();
    })

    $("#close_intro_cross").click( function(){
        $("#introductory_text").hide();
    });

    $("#logout_user").submit(function(){
        init_page(null, false, null);
    });


    $("#get_auth_form").submit(function(){
        username = $('#login_form')[0].value;
        password = $('#passwd_form')[0].value;
        url = GLOBAL_STATE.url + "/" + GLOBAL_STATE.auth_route + "/";
        sendAuthenticationRequest(url, username, password);
    });

    $("#get_list_user").click(function(){
        if (!is_logged()){
                showNotLoggedWarning();
        } else {
            url = GLOBAL_STATE.url + "/" + GLOBAL_STATE.user_route + "/";
            sendListUsersRequest( url, GLOBAL_STATE.token)
        }
    });

    $("#get_list_record").click(function(){
        if (!is_logged()){
                showNotLoggedWarning();
        } else {
            url = GLOBAL_STATE.url + "/" + GLOBAL_STATE.record_route + "/";
            sendListUsersRequest( url, GLOBAL_STATE.token)
        }
    });


    $("#create_user").click(function(){
        if (!GLOBAL_STATE.admin){
            alert("You tried to create an user but you're not an admin");
        }
    });

    $("#delete_user").click(function(){
        alert("You tried to delete user")
    });



});

