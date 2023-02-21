$(function(){

    function addDays(date, days) {
        var result = new Date(date);
        result.setDate(result.getDate() + days);
        return result;
    };


    Date.prototype.dayOfYear= function(){
        var j1= new Date(this);
        j1.setMonth(0, 0);
        return Math.round((this-j1)/8.64e7);
    };


    var clearRecordList = function(){
        $('#record_stat_list').empty();
        $(".unique_record").remove(); // remove all the records from the document
    };

    var clearUserList = function(){
        $("#user_list").empty(); // remove all the records from the document
    };

    var clearWindow = function (){
        refreshSelectors();
        cleanError();
        cleanSuccess();
        cleanWarning();
        clearRecordList();
        clearUserList();
    };



    var clearAuth = function(){
        $('#loggout_form').hide();
        $('#get_auth_form').show();
        $('#login_button').show();
        clearWindow();
        GLOBAL_STATE.user = null;
    };

    var setAuth = function(httpComing){
        $('#login_button').hide();
        $('#get_auth_form').hide();
        $('#loggout_form').show();
        clearWindow();
        GLOBAL_STATE.user = httpComing;
    };


    var error_callback = function(a,b,c){
        issueError(
            a.responseText + "<br><strong>Erreur " + a.status + "</strong>"
        );
    };


    var success_callback = function(data,status){
        issueSuccess(
            "<br><strong>HTTP status: " + status + "</strong>" + "<br>" +
             JSON.stringify(data)
        );
    };


    GLOBAL_STATE = {
        /* Strong convention to be followed:
        ** Nothing is to be followed. Just trust in the force.
        */
        url: "http://localhost:8000",
        auth_route: "api-token-auth",
        user_route: "users",
        record_route: "records",
        debug: true,
        user: null
    };


    var dataFromForm = function(data){
        // input data are usually objects returned by the jQuery .serializeArray()
        // method working on forms
        result = new Object();
        // use reduce to transform the data into a correct dictionary object
        data.reduce( function(a,b){
            a[b.name]=b.value;
            return a;
        }, result );

        return result;
    };


    var get_token = function(){

        if (GLOBAL_STATE.user && GLOBAL_STATE.user.token){
            var token = GLOBAL_STATE.user.token;
        } else {
            var token = null;
        }
        return token;
    };

    var usr_url = function(uid){
        url = GLOBAL_STATE.url + "/" + GLOBAL_STATE.user_route + "/";
        if (uid) {
            url = url + uid + "/";
        }
        return url;
    };


    var rec_url = function(rid){
        url = GLOBAL_STATE.url + "/" + GLOBAL_STATE.record_route + "/";
        if (rid) {
            url = url + rid + "/";
        }
        return url;
    };


    // ajax requests
    var sendAuthenticationRequest = function(url, username, password){
        var auth_callback = function(data, status) {
            issueSuccess("Successful Login!");
            setAuth(data);
        };
        $.ajax(url, {
            method: 'POST',
            data: { "username": username, "password": password },
            success: auth_callback,
            error: error_callback,
        });
    };


    var sendListRecordsRequest = function(url, token, callback){
        var record_list_callback = function(data, status){
            /* this callback function processes the API results */
            showSelectedRecords(data);
            success_callback(data, status);
        }
        /* perform AJAX request */
        if (!callback){
            callback=record_list_callback
        }

        $.ajax(url, {
            type: 'GET',
            // dataType: 'json',
            headers: { "Authorization": "Token " + token },
            processData: false,
            success: callback,
            error: error_callback,
        });
    };


    var sendListUsersRequest = function(url, token){
        var user_list_callback = function(data, status){
            /* this callback function processes the API results */
            showSelectedUsers(data);
            success_callback(data, status);
        }
        /* perform AJAX request */
        $.ajax(url, {
            type: 'GET',
            headers: { "Authorization": "Token " + token },
            processData: false,
            success: user_list_callback,
            error: error_callback,
        });
    };


    var addRequest = function(newData, url_route, callback){
        /* perform AJAX request */
        $.ajax( url_route, {
            type: 'POST',
            headers: { "Authorization": "Token " + GLOBAL_STATE.user.token },
            data: newData,
            success: success_callback,
            error: error_callback,
        });
    };


    var addUserRequest = function(newData){
        addRequest(newData, usr_url());
    };

    var addRecordRequest = function(newData){
        addRequest(newData, rec_url());
    };


    var updateRequest = function(url, token, newData){
        $.ajax( url, {
            type: 'PUT',
            headers: { "Authorization": "Token " + token },
            data: newData,
            success: success_callback,
            error: error_callback,
        });
    };


    var updateUserRequest = function(uid, newData){
        updateRequest(usr_url(uid), get_token(), newData);
    };

    var updateRecordRequest = function(uid, newData){
        updateRequest(rec_url(uid), get_token(), newData);
    };


    var deleteRequest = function(url, token, deleteCallback){
        /* perform AJAX request */
        $.ajax(url, {
            type: 'DELETE',
            headers: { "Authorization": "Token " + token },
            success: deleteCallback,
            error: error_callback,
        });
    };


    /* TODO: one could update dynamically the state of the page
    ** by also removing the corresponding form to this RECORD
    ** BUT this is additional complexity. Better to wait until
    ** everything is just fine
    */
    var deleteRecordRequest = function(rid){
        url = rec_url(rid);
        deleteRequest(url, get_token(), function(){
            success_callback();
            $('#unique_record_'+rid).remove();
        });
    };


    var deleteUserRequest = function(uid){
        url = usr_url(uid);
        deleteRequest(url, get_token(), function(){
            success_callback();
            $('#unique_user_'+uid).remove();
        });
    };

    // User Interface specific events and methods
    var issueWarning=function(message){
        $('#generic_warning').append('<p class="generic_warning_message"><strong>Warning! </strong>' + message + "</p>");
        $('#generic_warning').show();
    };

    // User Interface specific events and methods
    var issueError=function(message){
        $('#generic_error').show();
        $('#generic_error').append('<p class="generic_error_message"><strong>Error! </strong>' + message + "</p>");
    };

    // User Interface specific events and methods
    var issueSuccess=function(message){
        $('#generic_success').append('<p class="generic_success_message"><strong>Success! </strong>'+ message + '</p>');
        $('#generic_success').show();
    };


    $("#hide_generic_warning").click( function(){
        refreshSelectors();
        cleanWarning();
    });


    $('#hide_generic_success').click( function(){
        refreshSelectors();
        cleanSuccess();
    });

    refreshSelectors = function(){
        cleanWarning=function(){
            $(".generic_warning_message").remove();
            $("#generic_warning").hide();
        };
        cleanSuccess = function(){
            $(".generic_success_message").remove();
            $("#generic_success").hide();
        };
        cleanError = function(){
            $(".generic_error_message").remove();
            $("#generic_error").hide();
        };
    }
    $("#hide_generic_error").click( function(){
        refreshSelectors();
        cleanError();
    });


    $("#close_intro_cross").click( function(){
        $("#introductory_text").hide();
    });


    $("#help_button").click( function(){
        $("#introductory_text").show();
    });


    $("#record_list_cross").click( function(){
        clearRecordList();
    });


    $("#user_list_cross").click( function(){
        clearUserList();
    });


    $("#logout_button").click(function(){
        clearAuth();
    });


    $("#login_button").click(function(){
        var username = $('#login_form')[0].value;
        var password = $('#passwd_form')[0].value;
        var url = GLOBAL_STATE.url + "/" + GLOBAL_STATE.auth_route + "/";
        sendAuthenticationRequest(url, username, password);
    });


    $("#get_list_user").click(function(){
        sendListUsersRequest( usr_url(), get_token());
    });


    $("#get_list_record").click(function(){
        sendListRecordsRequest( rec_url(), get_token());
    });

    $("#filter_by_week").click(function(){
        // that's a big callback
        var filterByWeek = function(data, status){
            var date = $('#global_date')[0].valueAsDate;
            if (date){
                // 1 is monday, ..., 6 is saturday, 7 is sunday
                var day_of_week = (date.getDay()+6)%7 + 1 ;
                var max_date = addDays(date, 7-day_of_week);
                var min_date = addDays(date, -day_of_week+1);
                var is_between = function(record){
                    var record_Date = new Date(record.user_date);
                    return (record_Date < max_date && record_Date > min_date);
                };
                showSelectedRecords(data.filter( is_between ));
            } else {
                issueWarning("You must select a date with the date picker");
            }
        }
        // here is the request
        sendListRecordsRequest( rec_url(), get_token(), filterByWeek);
    });

    $('#create_new_record_button').click(function(){
        // fetch back the content of the form as an array
        addRecordRequest( dataFromForm( $('#new_record_form').serializeArray() ) );
    });

    $('#create_new_user_button').click( function(){
        // fetch back the content of the form as an array
        addUserRequest( dataFromForm( $('#new_user_form').serializeArray() ) );
    });


    var enableStats = function(recordList){
        var granTotal = recordList.reduce( function(a,b){ return (a + parseFloat(b.value)) ;}, 0);
        if (recordList.length){
            var maxDate = new Date(recordList[0].user_date);
            var minDate = new Date(recordList[0].user_date);
            for (i=1; i<recordList.length; i++){
                current_date = new Date(recordList[i].user_date);
                if ( current_date > maxDate ){
                    maxDate = current_date;
                }
                if ( current_date < minDate ){
                    minDate = current_date;
                }
            }
            numberOfYears = maxDate.getFullYear() - minDate.getFullYear();
            numberOfDays = maxDate.dayOfYear() - minDate.dayOfYear();
            // That is not really precise due to years with 366 days but it will do
            // with an adequate precision
            deltaInDays = 365*numberOfYears + numberOfDays;
            showStats(granTotal, deltaInDays+1);
        } else {
            showStats(granTotal, 1);
        }
    }

    var showStats = function(total, numberOfDays){
        if (numberOfDays > 0 ){
            var averageExpense = total / numberOfDays;
        } else {  // we don't want to divide per 0
            var averageExpense = total ;
        }
        $('#record_stat_list').empty();
        $('#record_stat_list').append(
            "<h3>Average expense running on <strong>"+
            numberOfDays+"</strong> days: <strong>You spent " +
            (averageExpense).toFixed(2) + " $ a day</strong></h3>"
        );
    }


    var showSelectedRecords = function(recordList){

        clearRecordList();

        var appendRecordToView = function( record ){
            $('#record_list').append('<li class="unique_record" id="unique_record_'+record.id+'">'+
            '<form id="unique_record_form_'+record.id+'" class="form-inline">'+
            '<input name="user_date" class="form-control" type="date"  value="'+record.user_date+ '" >'+
            '<input name="user_time" class="form-control" type="time"  value="'+record.user_time+ '" >'+
            '<input name="value" class="form-control" type="text"  value="'+record.value+ '" >'+
            '<input name="description" class="form-control" type="text"  value="'+record.description+ '" >'+
            '<input name="comment" class="form-control" type="text"  value="'+record.comment+ '" >'+
            '<button type="button" class="btn btn-warning update_record" value="' + record.id + '">update</button>' +
            '<button type="button" class="delete_record btn btn-danger" value="' + record.id + '">delete</button>' +
            '</form></li>');
        };

        recordList.map(appendRecordToView);
        enableStats(recordList);

        $(".delete_record").click( function(){
            deleteRecordRequest(this.value);
        });

        $(".update_record").click(function(){
            var newData = dataFromForm($('#'+this.parentNode.getAttribute('id')).serializeArray());
            updateRecordRequest(this.value, newData);
        });
    }


    var showSelectedUsers = function(userList){
        clearUserList();
        var appendUserToView = function( user ){
            if (user.is_staff){
                var is_staff="checked";
            }
            $('#user_list').append(
                '<li id="unique_user_'+user.id+'">'+
                '<form id="unique_user_form_'+user.id+'" class="form-inline">'+
                    '<input type="checkbox" onclick="return false" name="is_staff" class="form-control" ' + is_staff + '>' +
                    '<input name="first_name" class="form-control" type="text" placeholder="firstname" value="' + user.first_name + '" >' +
                    '<input name="last_name" class="form-control" type="text" placeholder="lastname" value="' + user.last_name + '" >' +
                    '<input name="username" class="form-control" type="text" placeholder="username" value="' + user.username + '" >' +
                    '<input name="password" class="form-control" type="text" placeholder="password" value="" >' +
                    '<button type="button" class="btn btn-warning update_user" value="' + user.id +'">update</button>' +
                    '<button type="button" class="btn btn-danger delete_user" value="' + user.id +'">delete</button>' +
                '</form></li>'
            );
        };

        userList.map(appendUserToView);

        $(".delete_user").click(function(){
            deleteUserRequest(this.value);
        });

        $(".update_user").click(function(){
            var newData = dataFromForm($('#'+this.parentNode.getAttribute('id')).serializeArray());
            updateUserRequest(this.value, newData);
        });
    }

});

