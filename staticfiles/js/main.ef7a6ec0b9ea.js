$(document).ready(function(){
	console.log("Hi there!")
    $('.parallax').parallax();
    $('.slider').slider();

  $('.button-collapse').sideNav({
      edge: 'left', 
      closeOnClick: true // Closes side-nav on <a> clicks, useful for Angular/Meteor
    });

///// Create /////
    $('#nav').on('click', "#add", function(event){
        event.preventDefault();

        var template = $('#create-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);  
        window.scrollTo(0, 0);
    });

    $('#answer_div').on('click', "#add", function(event){
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
    $('#nav').on('click', "#top", function(event){
    event.preventDefault();

    $.ajax({
        method: "GET",
        url: "top",
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

///// View All /////
    $('#answer_div').on('click', "#top", function(event){
    event.preventDefault();

    $.ajax({
        method: "GET",
        url: "top",
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
        var score_id = ($(this).find("[name='delete_id']").attr("value")); // find tells it where in the this object to look for the value

        $.ajax({
            method: "POST",
            url: ("delete/" + score_id),
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

    

});