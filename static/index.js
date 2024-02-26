$(document).ready(function() {
    $(".desc").waypoint(function(){
        $(".desc").addClass("animate__animated animate__fadeInLeft")
    }, {offset: "80%"})

    $(".forms").waypoint(function(){
        $(".forms").addClass("animate__animated animate__backInUp")
    }, {offset: "80%"})

    $(".viewer").waypoint(function(){
        $(".viewer").addClass("animate__animated animate__fadeInRight")
    }, {offset: "80%"})
})