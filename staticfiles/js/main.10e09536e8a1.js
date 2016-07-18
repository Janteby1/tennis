$(document).ready(function(){
	console.log("Hi there!")
    $('.parallax').parallax();
    $('.slider').slider();

  $('.button-collapse').sideNav({
      edge: 'left', 
      closeOnClick: true // Closes side-nav on <a> clicks, useful for Angular/Meteor
    });

///// User Register /////
    $('#nav').on('click', "#register", function(event){
    	event.preventDefault();
        var template = $('#user_register-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);
    });

    $('#answer_div').on('submit', '#user_register_form',function(event){
    event.preventDefault();

    var query_string = $(this).serialize() // returns all the data in your form

    $.ajax({
        method: "POST",
        url: "user_register",
        data: query_string,
    }).done(function(data, status){

		if (data.success){
			////// if they registered then display the Login ////////
                var template = $('#user_login-template').html();
		        var renderM = Mustache.render(template);
		        $('#answer_div').html(renderM);
            }
        });
    });


///// Org Register /////
    $('#nav').on('click', "#add_org", function(event){
        event.preventDefault();
        var template = $('#org_register-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);
    });

    $('#answer_div').on('submit', '#org_register_form',function(event){
    event.preventDefault();

    var query_string = $(this).serialize() // returns all the data in your form

    $.ajax({
        method: "POST",
        url: "org_register",
        data: query_string,
    }).done(function(data, status){

        if (data.success){
            ////// if they registered then display the Login ////////
                var template = $('#org_added-template').html();
                var renderM = Mustache.render(template);
                $('#answer_div').html(renderM);
            }
        });
    });



///// User Login /////
    $('#nav').on('click', "#login", function(event){
    	event.preventDefault();
        var template = $('#user_login-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);
    });

    $('#answer_div').on('submit', '#user_login_form',function(event){
    event.preventDefault();

    var query_string = $(this).serialize() // returns all the data in your form

    $.ajax({
        method: "POST",
        url: "user_login",
        data: query_string,
    }).done(function(data, status){

          if (data.success){
          ////// if they login correctly ////////
            console.log("HERE")
            document.location.href="/";
            window.scrollTo(0, 0);
        	} 
    	});
    });


///// Logout /////
    $('#nav').on('click', "#logout", function(event){
    event.preventDefault();

    $.ajax({
        method: "POST",
        url: "logout",
        // data: query_string,
    }).done(function(data, status){

	location.reload();
    });
});


///// About /////
    $('#nav').on('click', "#about", function(event){
        event.preventDefault();
        var template = $('#about-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);
    });


///// Create /////
    $('#nav').on('click', "#add", function(event){
        event.preventDefault();

        var template = $('#create-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);  
        window.scrollTo(0, 0);
    });


    $('#answer_div').on('submit', '#create_form',function(event){
    event.preventDefault();

    var query_string = $(this).serialize() //returns all the data in your form
    console.log(query_string)

    $.ajax({
        method: "POST",
        url: "add",
        data: query_string,
    }).done(function(data, status){

    if (data.success){
        console.log(data.Message)
        event_id = data.id
        // console.log(data.id)
        var template = $('#tags-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);  
        window.scrollTo(0, 0);
        }
    else {
        var template = $('#403-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);  
        window.scrollTo(0, 0);
            }
        });
    });

    // add tags //
    $('#answer_div').on('submit', '#tags_form',function(event){
    event.preventDefault();

    var query_string = $(this).serialize() //returns all the data in your form
    console.log(query_string)
    console.log(event_id)

    $.ajax({
        method: "POST",
        url: ("tags/" + event_id),
        data: query_string,
    }).done(function(data, status){

    if (data.success){
        console.log(data.Message)
        var template = $('#thanx-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);  
        window.scrollTo(0, 0);
        }
    else {
        var template = $('#403-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);  
        window.scrollTo(0, 0);
            }
        });
    });


///// View All /////
    $('#nav').on('click', "#all", function(event){
    event.preventDefault();

    $.ajax({
        method: "GET",
        url: "all",
        // data: query_string,
    }).done(function(data, status){

    if (data.success){
        var template = $('#results-template').html();
        var renderM = Mustache.render(template, {"results":data.results});
        $('#answer_div').html(renderM);  
        window.scrollTo(0, 0);
        }
    else {
        var template = $('#403-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);  
        window.scrollTo(0, 0);
            }
        });
    });


//// Delete Button ////
    $('#answer_div').on('submit', ".delete_button_form", function(event){
    event.preventDefault();

    var check = confirm("Are you sure you want to delete this event?");

    if (check == true) {
        var delete_id = ($(this).find("[name='delete_id']").attr("value")); // find tells it where in the this object to look for the value

        $.ajax({
            method: "POST",
            url: ("delete/" + delete_id),
            // data: query_string,
        }).done(function(data, status){

            if (data.success){
                ////// if answers came back ////////
                alert("Ok, Event Deleted \nRefresh page to see updated results");
                window.scrollTo(0, 0);
            } else {
                var template = $('#403-template').html();
                var renderM = Mustache.render(template);
                $('#answer_div').html(renderM);  
                window.scrollTo(0, 0);
            }
            });

    } else {
        alert("Ok, Event will be kept");
    }
});


//// Vote Up / Like Button ////
    $('#answer_div').on('submit', ".vote_up_button_form", function(event){
    event.preventDefault();

    var check = confirm("Would you like to UP vote this event?");

    if (check == true) {
        var vote_id = ($(this).find("[name='vote_id']").attr("value")); // find tells it where in the this object to look for the value

        $.ajax({
            method: "POST",
            url: ("vote_up/" + vote_id),
            // data: query_string,
        }).done(function(data, status){

            if (data.success){
                ////// if answers came back ////////
                alert("Event UP voted! \nThank you! ");
                window.scrollTo(0, 0);
            } else {
                var template = $('#403-template').html();
                var renderM = Mustache.render(template);
                $('#answer_div').html(renderM);  
                window.scrollTo(0, 0);
            }
            });

    } else {
        alert("Ok, Event idea will be kept");
    }
    });


//// Vote Down Button ////
    $('#answer_div').on('submit', ".vote_down_button_form", function(event){
    event.preventDefault();

    var check = confirm("Would you like to DOWN vote this event?");

    if (check == true) {
        var vote_id = ($(this).find("[name='vote_id']").attr("value")); // find tells it where in the this object to look for the value

        $.ajax({
            method: "POST",
            url: ("vote_down/" + vote_id),
            // data: query_string,
        }).done(function(data, status){

            if (data.success){
                ////// if answers came back ////////
                alert("Event DOWN voted! \nThank you! ");
                window.scrollTo(0, 0);
            } else {
                var template = $('#403-template').html();
                var renderM = Mustache.render(template);
                $('#answer_div').html(renderM);  
                window.scrollTo(0, 0);
            }
            });

    } else {
        alert("Ok, Event idea will be kept");
    }
    });


// Create Button //
    $('#answer_div').on('click', "#create_button", function(event){
      event.preventDefault();
        var template = $('#create-template').html();
        var renderM = Mustache.render(template, {});
        $('#answer_div').html(renderM);
        window.scrollTo(0, 0);
    });


///// Manage My Tags /////
    $('#answer_div').on('click', "#my_tags", function(event){
        event.preventDefault();

        var template = $('#my-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);  
        window.scrollTo(0, 0);
    });

    $('#answer_div').on('submit', '#my_tags_form',function(event){
    event.preventDefault();

    var query_string = $(this).serialize() //returns all the data in your form
    console.log(query_string)

    $.ajax({
        method: "POST",
        url: "my_tags",
        data: query_string,
    }).done(function(data, status){

    if (data.success){
        console.log(data.Message)
        var template = $('#thanx-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);  
        window.scrollTo(0, 0);
        }
    else {
        var template = $('#403-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);  
        window.scrollTo(0, 0);
            }
        });
    });


///// View My Events /////
    $('#nav').on('click', "#my", function(event){
        event.preventDefault();

    var query_string = $(this).serialize() //returns all the data in your form
    // console.log(query_string)

    $.ajax({
        method: "GET",
        url: "my",
        data: query_string,
    }).done(function(data, status){

    if (data.success){
        var template = $('#my-results-template').html();
        var renderM = Mustache.render(template, {"results":data.results});
        $('#answer_div').html(renderM);  
        window.scrollTo(0, 0);
        }
    else {
        var template = $('#403-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);  
        window.scrollTo(0, 0);
            }
        });
    });


//// RSVP Button ////
    $('#answer_div').on('submit', ".rsvp_button_form", function(event){
    event.preventDefault();

    var check = confirm("Are you sure you want to go this event?");

    if (check == true) {
        var rsvp_id = ($(this).find("[name='rsvp_id']").attr("value")); // find tells it where in the this object to look for the value

        $.ajax({
            method: "POST",
            url: ("rsvp/" + rsvp_id),
            // data: query_string,
        }).done(function(data, status){

            if (data.success){
                ////// if answers came back ////////
                alert("Ok, RSVP Recorded \nPlease make sure to also sign up through ornaization websites if needed!");
                window.scrollTo(0, 0);
            } else {
                var template = $('#403-template').html();
                var renderM = Mustache.render(template);
                $('#answer_div').html(renderM);  
                window.scrollTo(0, 0);
            }
            });

    } else {
        alert("Ok, maybe try another event.");
    }
});




    

});