

$(function(){
    var globalAjaxSettings = {
      async: false,
      accepts: 'json'
    }

    DATE_PICKER = $('#datetimepicker1');
    DATE_PICKER.datetimepicker();

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

    USER_LIST = null;
    RECORD_LIST = null;

    SELECTED_USERS = null;
    SELECTED_RECORDS = null;

    var usr_url = function(uid){
        url = GLOBAL_STATE.url + "/" + GLOBAL_STATE.user_route + "/";
        if (uid) {
            url = url + uid + "/";
        }
        return url;
    }

    var rec_url = function(rid){
        url = GLOBAL_STATE.url + "/" + GLOBAL_STATE.record_route + "/";
        if (rid) {
            url = url + rid + "/";
        }
        return url;
    }

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
    // for debugging purpose
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

    var deleteRecordRequest = function(url, token){
        var delete_user_callback = function(data, status){
            /* this callback function processes the API results */
            LAST_HTTP_ANSWER = data;
            debug();
        }
        /* perform AJAX request */
        $.ajax(url, {
            type: 'DELETE',
            headers: { "Authorization": "Token " + token },
            success: record_list_callback,
        });
    }

    var updateUserRequest = function(url, uid, token, newData){
        var update_user_callback = function(data, status){
            /* this callback function processes the API results */
            LAST_HTTP_ANSWER = data;
            debug();
        }
        /* perform AJAX request */

        var url_route = user_url(uid);
        $.ajax( url_route, {
            type: 'PUT',
            headers: { "Authorization": "Token " + token },
            data: newData,
            success: user_list_callback,
        });
    }


    var updateRecordRequest = function(rid, newData){
        var update_user_callback = function(data, status){
            /* this callback function processes the API results */
            LAST_HTTP_ANSWER = data;
            debug();
        }
        /* perform AJAX request */
        var url_route = rec_url(rid);
        $.ajax( url_route, {
            type: 'PUT',
            headers: { "Authorization": "Token " + GLOBAL_STATE.token },
            data: newData,
            success: user_list_callback,
        });
    }

    var deleteUserRequest = function(uid){
        var delete_user_callback = function(data, status){
            /* this callback function processes the API results */
            LAST_HTTP_ANSWER = data;
            debug();
        }
        /* perform AJAX request */
        url_route = usr_url(uid)
        $.ajax(url_route, {
            type: 'DELETE',
            headers: { "Authorization": "Token " + GLOBAL_STATE.token },
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

    $("#record_list_cross").click( function(){
        clearRecordList();
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

    var filterAgainstWeek = function(){
        date = DATE_PICKER.data("DateTimePicker").date();
        day_of_week = date.isoWeekday() ; // 1 is monday, ..., 7 is sunday
        if (date){
            var max_date = date.add(7-day_of_week, 'days');
            var min_date = date.subtract(day_of_week-1, 'days');
            var is_between = function(record){ return moment(record.user_date).isBetween(min_date, max_date);
            SELECTED_RECORDS = RECORD_LIST.filter( is_between );
            showSelectedRecords();
        }
    }
        // if no date is set, there is nothing to filter
    }
    var filterAgainstYear = function(){
        date = DATE_PICKER.data("DateTimePicker").date();
        if (date){
            var max_date = date.add(7-day_of_week, 'days');
            var min_date = date.subtract(day_of_week-1, 'days');
            var is_between = function(record){ return moment(record.user_date).isBetween(min_date, max_date) };
            showSelectedRecords(RECORD_LIST.filter( is_between ));
        }
    }

    var clearRecordList = function(){
        $("#record_list").empty(); // remove all the records from the document
    }



    var enableStats = function(recordList){
        var granTotal = recordList.reduce( function(a,b){ return a.amount + b.amount ;}, 0);

        if (recordList.length && granTotal){
            var maxDate = recordList[0].user_date;
            var minDate = recordList[0].user_date;
            for (i=1; i<recordList.length; i++){
                if (moment(recordList[i].user_date).isAfter(maxDate, 'day')){
                    maxDate = moment(recordList[i]);
                }
                if (moment(recordList[i]).isBefore(minDate, 'day')){
                    minDate = moment(recordList[i].user_date)
                }
            }
            numberOfDays = maxDate.subtract(minDate).days()
            showStats(granTotal, numberOfDays);
        } else {
            showStats(granTotal, 1);
        }
    }

    var showStats = function(total, numberOfDays){
        if (numberOfDays > 0 ){
            var averageExpense = total / numberOfDays;
        } else {
            // we don't want to divide per 0
            var averageExpense = total ;
        }
        $('#record_stat_list').empty();
        $('#record_stat_list').append("<ul id=\"record_stat_list\">\n"+
        "<li>Average expense per day: " + averageExpense + "</li>\n"+
        "<li>Average running on " + numberOfDays + " days</li>\n" + "</ul>\n")
    }


    var showSelectedRecords = function(recordList){
        clearRecordList();
        var appendRecordToView = function( record ){
            $('.record').after("<li class=\"unique_record\">"+record.user_date+"</li>")
        };
        recordList.map(appendRecordToView);
        enableStats(recordList);
    }

    var deleteCheckedRecords = function(){
        // must read the DOM to call delete Record on the selected records
        // easy
        var i=0;
    }

    var deleteCheckedUsers = function(){
        // must read the DOM to call delete Record on the selected users
        var i=0;
    }

});

