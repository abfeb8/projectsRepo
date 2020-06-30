// check off specific todos when clicked
$("ul").on("click", "li", function () {
    $(this).toggleClass("todoComplete");
});

// click X to delet todo
$("ul").on("click", "li span", function (event) {
    $(this)
        .parent()
        .fadeOut(500, function () {
            $(this).remove();
        });
    event.stopPropagation();
});

// to get value from the input
$("input").on("keypress", function (event) {
    if (event.which == 13) {
        //grabbing new todo from the input
        text = $(this).val();
        $(this).val("");
        //creating a new li in the ul
        $("ul").append(
            "<li><span><i class='fa fa-trash' aria-hidden='true'></i></span> " +
                text +
                "</li>"
        );
    }
});

//adding click event on the plus icon
$(".fa-plus").click(function () {
    $("input").fadeToggle(500);
});
