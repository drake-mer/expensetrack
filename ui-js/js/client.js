

GLOBAL_STATE = {
  logged: false,
  admin: false,
  url: "http://localhost:8000"
}

var globalAjaxSettings = {
  async: false,
  accepts: 'json'
}

var readState = function(state){
  return state;
}

var checkSession = function(){
  return true;
}

var setAdminUI = function(state){
  state["admin"]=true;
  state["can_delete_user"]=true;
  state["can_query_any_user"]=true;
  state["can_query_any_record"]=true;
  state["can_create_user"]=true;
  return state;
}


$(document).ready(function(){

    $(".close").click( function(){
        $(".close").parent().alert("close");
    });

    $("#login").click(function(){
        alert("You tried to login")
    });

    $("#create_user").click(function(){
        alert("You tried to create user")
    });

    $("#delete_user").click(function(){
        alert("You tried to delete user")
    });
});



var displayNotLogged = function(){
  $("#alert_not_logged").alert(); 
}






var getUserRecords = function ( user_id ){
  if (!readState().logged) {
    console.log("You must be logged into your account to fetch data for this user")
  } else if (!checkSession()) {
    state["logged"]=false;
    getUserRecords();
  } else {

  }
}


var displayRecords = function(){
  alert('Here are the records');
}

var displayProblems = function(){
  alert('there has been a problem')
}

var displayEndRequest = function(){
  alert('Request has been sent and processed')
}

var queryUser = function( user_id ) {
  $.ajax({
    url: ( state["url_tracker"] + "/user/" + user_id ),
    data: { is_authenticated: true },
    method: 'GET',
    dataType: 'json',
    success: displayRecords,
    error: displayProblem,
    complete: displayEndRequest   
  })
}

