$(function(){

    function addDays(date, days) {
        var result = new Date(date);
        result.setDate(result.getDate() + days);
        return result;
    }

    Date.prototype.dayOfYear= function(){
        var j1= new Date(this);
        j1.setMonth(0, 0);
        return Math.round((this-j1)/8.64e7);
    }

    var clearRecordList = function(){
        $('#record_stat_list').empty();
        $(".unique_record").remove(); // remove all the records from the document
    }

    var clearUserList = function(){
        $("#user_list").empty(); // remove all the records from the document
    }

    clean_warning = function (){
        $("#generic_warning").hide();
        $("#generic_error").hide();
        $("#generic_success").hide();
        clearAuth();
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

    var clearAuth = function(){

        $('#loggout_form').hide();
        $('#logging_form').show();
        GLOBAL_STATE.user = null;
    };

    var setAuth = function(httpComing){
        $('#loggout_form').show();
        $('#logging_form').hide();
        GLOBAL_STATE.user = httpComing;
    };


    var is_logged = function(){
        return GLOBAL_STATE.logged;
    };

    GLOBAL_STATE = {
        /* Strong convention to be followed:
        ** Only the init_page() function may modify this object
        ** Other method can read it for convenience but should never be used to set fields values
        ** When the global state has to be changed, one has to call init_page() with adequate
        ** parameters.
        */
        url: "http://localhost:8000",
        auth_route: "api-token-auth",
        user_route: "users",
        record_route: "records",
        debug: true,
        user: null
    };


    var get_token = function(){

        if (GLOBAL_STATE.user){
            var token = GLOBAL_STATE.user.token;
        } else {
            var token = null;
        }
        return token;
    }

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
    }


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


    var updateUserRequest = function(url, token, newData){
        $.ajax( url, {
            type: 'PUT',
            headers: { "Authorization": "Token " + token },
            data: newData,
            success: success_callback,
            error: error_callback,
        });
    };

    var updateUserRequest = function(uid, newData){
        updateRequest(usr_url(uid), GLOBAL_STATE.user.token, newData)
    };

    var updateUserRequest = function(uid, newData){
        updateRequest(rec_url(uid), GLOBAL_STATE.user.token, newData)
    };



    var deleteRequest = function(url, token){

        /* perform AJAX request */
        $.ajax(url, {
            type: 'DELETE',
            headers: { "Authorization": "Token " + token },
            success: success_callback,
            error: error_callback,
        });
    } ;

    var deleteRecordRequest = function(rid){
        url = rec_url(rid);
        deleteRequest(url, get_token());
    };


    var deleteUserRequest = function(uid){
        url = usr_url(uid);
        deleteRequest(url, get_token());
    };


    // User Interface specific events and methods
    var issueWarning=function(message){
        // $('.generic_warning_message').remove();
        $('#generic_warning').append('<p class="generic_warning_message"><strong>Warning! </strong>'+message+"</p>");
        $('#generic_warning').show();
    };

    // User Interface specific events and methods
    var issueError=function(message){
        // $('.generic_error_message').remove();
        $('#generic_error').append('<p class="generic_error_message"><strong>Error! </strong>'+message+"</p>");
        $('#generic_error').show();
    };

    // User Interface specific events and methods
    var issueSuccess=function(message){
        // $('.generic_success_message').remove();
        $('#generic_success').append('<p class="generic_sucess_message"><strong>Success! </strong>'+message+"</p>");
        $('#generic_success').show();
    };

    $("#hide_generic_warning").click( function(){
        $("#generic_warning").hide();
    });

    $('#hide_generic_success').click( function(){
        $("#generic_success").hide();
    });

    $("#hide_generic_error").click( function(){
        $("#generic_error").hide();
    });

    $("#close_intro_cross").click( function(){
        $("#introductory_text").hide();
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
                var day_of_week = date.getDay() ; // 0 is monday, ..., 6 is sunday
                var max_date = addDays(date, 6-day_of_week);
                var min_date = addDays(date, -day_of_week);
                var is_between = function(record){
                    var record_Date = new Date(record.user_date);
                    return (record_Date <= max_date && record_Date >= min_date);
                };
                showSelectedRecords(data.filter( is_between ));
            } else {
                issueWarning("You must select a date with the date picker");
            }
        }
        // here is the request
        sendListRecordsRequest( rec_url(), get_token(), filterByWeek);
    });

    $('#new_record_form').click(function(){
        // fetch back the content of the form as an array
        var newDataFromForm = $('#new_record_form').serializeArray();
        result = new Object();

        // use reduce to transform the data into a correct dictionary object
        newDataFromForm.reduce(function(a,b){
            a[b.name]=b.value;
            return a;
        }, result);
        addRecordRequest( result );
    });

    $('#new_user_form').click(function(){
        // fetch back the content of the form as an array
        var newDataFromForm = $('#new_user_form').serializeArray();
        result = new Object();

        // use reduce to transform the data into a correct dictionary object
        newDataFromForm.reduce(function(a,b){
            a[b.name]=b.value;
            return a;
        }, result);
        addUserRequest( result );
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
        numberOfDays+"</strong> days: <strong>" +
        (averageExpense).toFixed(2) + " $/day</strong></h3>"
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

        $(".delete_record").click(function(){
            alert("You tried to delete record");
        });

        $(".update_record").click(function(){
            alert("You tried to update record");
        });
    }


    var showSelectedUsers = function(userList){
        clearUserList();
        var appendUserToView = function( user ){
            if (user.is_staff){
                var is_staff="checked";
            }
            $('#user_list').append(
                '<div class="unique_user_'+user.id+'">'+
                '<form id="unique_user_form_'+user.id+'" class="form-inline">'+
                    '<input type="checkbox" onclick="return false" name="is_staff" class="form-control" ' + is_staff + '>' +
                    '<input name="first_name" class="form-control" type="text" placeholder="firstname" value="' + user.first_name + '" >' +
                    '<input name="last_name" class="form-control" type="text" placeholder="lastname" value="' + user.last_name + '" >' +
                    '<input name="username" class="form-control" type="text" placeholder="username" value="' + user.username + '" >' +
                    '<input name="password" class="form-control" type="text" placeholder="password" value="" >' +
                    '<button type="button" class="btn btn-warning update_user" value="' + user.id +'">update</button>' +
                    '<button type="button" class="btn btn-danger delete_user" value="' + user.id +'">delete</button>' +
                '</form></div>'
            );
        };
        userList.map(appendUserToView);

        $(".delete_user").click(function(){
            deleteUserRequest(this.value);

        });

        $(".update_user").click(function(){
            updateUserRequest(this.value);
        });
    }
    /* for debugging purpose */
    setAuth( { username:'david', is_staff: true, id: 1,
               token:"b4a8a313eb062dbff8c7b9cfee28e9bcfddb9dc8" } );
});

